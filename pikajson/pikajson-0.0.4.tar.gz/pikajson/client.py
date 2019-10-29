import configparser
import sys
import time
import uuid

import pika
import logging
import json

logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.DEBUG)
logging.getLogger('pika').setLevel(logging.WARNING)


class PikaPublisher:

    reconnection_timeout = 5

    # WARNING pika is not thread safe, so use one sender instance for one thread
    def __init__(self, queue, host, port, user, password):
        self._queue = queue
        self._host = host
        self._port = port
        self._user = user
        self._pass = password
        self._connection = None
        self._channel = None
        self.connected = False
        self.connect()

    @classmethod
    def create_from_config(cls, config_path, config_section='publisher'):
        config = configparser.ConfigParser()
        config.readfp(open(config_path))
        queue = config.get(config_section, "queue")
        host = config.get(config_section, "host")
        port = config.get(config_section, "port")
        user = config.get(config_section, "user")
        password = config.get(config_section, "password")
        return cls(queue, host, port, user, password)

    def connect(self, timeout=1000.0):
        start_time = time.time()
        while not self.connected:
            try:
                credentials = pika.PlainCredentials(self._user, self._pass)
                parameters = pika.ConnectionParameters(host=self._host, port=self._port, credentials=credentials)
                self._connection = pika.BlockingConnection(parameters)
                self._channel = self._connection.channel()
                self._channel.queue_declare(queue=self._queue, durable=True)
                self._channel.confirm_delivery()
                self.connected = True
            except Exception as ex:
                if time.time()-start_time > timeout:
                    logging.error("connecting error: %s" % (str(ex)),
                                  extra={"queue": self._queue, "host": self._host})
                    raise ex
                logging.error("connecting error: %s, reconnecting in %d seconds..." %
                              (str(ex), self.reconnection_timeout),
                              extra={"queue": self._queue, "host": self._host})
                time.sleep(self.reconnection_timeout)

    def disconnect(self):
        self.connected = False
        if self._connection is not None and not self._connection.is_closed:
            try:
                self._connection.close()
            except Exception as ex:
                logging.error("rabbit disconnect error: %s" % str(ex),
                              extra={"queue": self._queue, "host": self._host})

    def publish(self, message, timeout=1000.0):
        try:
            start_time = time.time()
            if "rmq_unique" not in message.keys():
                message["rmq_unique"] = str(uuid.uuid4())
            body = json.dumps(message)
            sent = False
            while not sent:
                try:
                    self._channel.basic_publish(exchange='', routing_key=self._queue, body=body,
                                            properties=pika.BasicProperties(
                                                 delivery_mode=2,
                                            ), mandatory=True)
                    sent = True
                except Exception as ex:
                    if time.time() - start_time > timeout:
                        logging.error("publish error: %s" % (str(ex)),
                                      extra={"queue": self._queue, "host": self._host})
                        self.disconnect()
                        raise ex
                    logging.error("publish error: %s, reconnecting in %d seconds..." %
                                  (str(ex), self.reconnection_timeout),
                                  extra={"queue": self._queue, "host": self._host})
                    self.disconnect()
                    time.sleep(self.reconnection_timeout)
                    self.connect(timeout)
        except Exception as ex:
            logging.error("rabbit publish error in line %s: %s" % (str(sys.exc_info()[-1].tb_lineno), str(ex)),
                          extra={"queue": self._queue, "message": message})
            raise ex

    def __del__(self):
        self.disconnect()

import re

from pygments.lexer import RegexLexer, words
from pygments.token import Keyword, Text, Comment, Name, Number, Operator, String, Punctuation

from spannercli import commands

#: SQL Syntax https://cloud.google.com/spanner/docs/query-syntax#sql-syntax
syntax = (
    "ORDER BY",
    "ASC",
    "DESC",
    "LIMIT",
    "OFFSET",
    "SELECT",
    "ALL",
    "DISTINCT",
    "AS",
    "FROM",
    "WHERE",
    "GROUP BY",
    "HAVING",
    "UNION",
    "DISTINCT",
    "INTERSECT",
    "EXCEPT",
    "UNNEST",
    "WITH",
    "FORCE_INDEX",
    "GROUPBY_SCAN_OPTIMIZATION",
    "JOIN",
    "ON",
    "USING",
    "INNER",
    "CROSS",
    "FULL",
    "OUTER",
    "LEFT",
    "RIGHT",
    "HASH",
    "FORCE_JOIN_ORDER",
    "JOIN_METHOD",
    "TABLESAMPLE",
    "BERNOULLI",
    "RESERVOIR",
    "PERCENT",
    "ROWS",
    # https://cloud.google.com/spanner/docs/dml-syntax
    "INSERT INTO",
    "VALUES",
    "DEFAULT",
    "DELETE",
    "UPDATE",
)

#: Reserved Keywords https://cloud.google.com/spanner/docs/lexical#reserved-keywords
keywords = (
    "ALL",
    "AND",
    "ANY",
    "ARRAY",
    "AS",
    "ASC",
    "ASSERT_ROWS_MODIFIED",
    "AT",
    "BETWEEN",
    "BY",
    "CASE",
    "CAST",
    "COLLATE",
    "CONTAINS",
    "CREATE",
    "CROSS",
    "CUBE",
    "CURRENT",
    "DEFAULT",
    "DEFINE",
    "DESC",
    "DISTINCT",
    "ELSE",
    "END",
    "ENUM",
    "ESCAPE",
    "EXCEPT",
    "EXCLUDE",
    "EXISTS",
    "EXTRACT",
    "FALSE",
    "FETCH",
    "FOLLOWING",
    "FOR",
    "FROM",
    "FULL",
    "GROUP",
    "GROUPING",
    "GROUPS",
    "HASH",
    "HAVING",
    "IF",
    "IGNORE",
    "IN",
    "INNER",
    "INTERSECT",
    "INTERVAL",
    "INTO",
    "IS",
    "JOIN",
    "LATERAL",
    "LEFT",
    "LIKE",
    "LIMIT",
    "LOOKUP",
    "MERGE",
    "NATURAL",
    "NEW",
    "NO",
    "NOT",
    "NULL",
    "NULLS",
    "OF",
    "ON",
    "OR",
    "ORDER",
    "OUTER",
    "OVER",
    "PARTITION",
    "PRECEDING",
    "PROTO",
    "RANGE",
    "RECURSIVE",
    "RESPECT",
    "RIGHT",
    "ROLLUP",
    "ROWS",
    "SELECT",
    "SET",
    "SOME",
    "STRUCT",
    "TABLESAMPLE",
    "THEN",
    "TO",
    "TREAT",
    "TRUE",
    "UNBOUNDED",
    "UNION",
    "UNNEST",
    "USING",
    "WHEN",
    "WHERE",
    "WINDOW",
    "WITH",
    "WITHIN",
)

#: Data types https://cloud.google.com/spanner/docs/data-definition-language#data_types
datatypes = (
    "BOOL",
    "INT64",
    "FLOAT64",
    "STRING",
    "BYTES",
    "DATE",
    "TIMESTAMP",
)

#: Function https://cloud.google.com/spanner/docs/functions-and-operators
# _roughly_ obtain function list from above url with this script.
# ```javascript
# var items = $$("h3");
# for (each in items){
#    var s = items[each].textContent;
#    if (s.match(/^[A-Z0-9_]+$/)) {
#        console.log(items[each].textContent);
#    }
# }
# ```
functions = (
    # Aggregate functions
    "ANY_VALUE",
    "ARRAY_AGG",
    "AVG",
    "BIT_AND",
    "BIT_OR",
    "BIT_XOR",
    "COUNT",
    "COUNTIF",
    "LOGICAL_AND",
    "LOGICAL_OR",
    "MAX",
    "MIN",
    "STRING_AGG",
    "SUM",
    # Mathematical functions
    "ABS",
    "SIGN",
    "IS_INF",
    "IS_NAN",
    "IEEE_DIVIDE",
    "SQRT",
    "POW",
    "POWER",
    "EXP",
    "LN",
    "LOG",
    "LOG10",
    "GREATEST",
    "LEAST",
    "DIV",
    "MOD",
    "ROUND",
    "TRUNC",
    "CEIL",
    "CEILING",
    "FLOOR",
    "COS",
    "COSH",
    "ACOS",
    "ACOSH",
    "SIN",
    "SINH",
    "ASIN",
    "ASINH",
    "TAN",
    "TANH",
    "ATAN",
    "ATANH",
    "ATAN2",
    # Hash functions
    "FARM_FINGERPRINT",
    "SHA1",
    "SHA256",
    "SHA512",
    # String functions
    "BYTE_LENGTH",
    "CHAR_LENGTH",
    "CHARACTER_LENGTH",
    "CODE_POINTS_TO_BYTES",
    "CODE_POINTS_TO_STRING",
    "CONCAT",
    "ENDS_WITH",
    "FORMAT",
    "FROM_BASE64",
    "FROM_HEX",
    "LENGTH",
    "LPAD",
    "LOWER",
    "LTRIM",
    "REGEXP_CONTAINS",
    "REGEXP_EXTRACT",
    "REGEXP_EXTRACT_ALL",
    "REGEXP_REPLACE",
    "REPLACE",
    "REPEAT",
    "REVERSE",
    "RPAD",
    "RTRIM",
    "SAFE_CONVERT_BYTES_TO_STRING",
    "SPLIT",
    "STARTS_WITH",
    "STRPOS",
    "SUBSTR",
    "TO_BASE64",
    "TO_CODE_POINTS",
    "TO_HEX",
    "TRIM",
    "UPPER",
    # JSON functions
    "JSON_QUERY",
    "JSON_VALUE",
    # Array functions
    "ARRAY",
    "ARRAY_CONCAT",
    "ARRAY_LENGTH",
    "ARRAY_TO_STRING",
    "GENERATE_ARRAY",
    "GENERATE_DATE_ARRAY",
    "ARRAY_REVERSE",
    "SAFE_OFFSET",
    "SAFE_ORDINAL",
    # Date functions
    "CURRENT_DATE",
    "EXTRACT",
    "DATE",
    "DATE_ADD",
    "DATE_SUB",
    "DATE_DIFF",
    "DATE_TRUNC",
    "DATE_FROM_UNIX_DATE",
    "FORMAT_DATE",
    "PARSE_DATE",
    "UNIX_DATE",
    # Timestamp functions
    "CURRENT_TIMESTAMP",
    "EXTRACT",
    "STRING",
    "TIMESTAMP",
    "TIMESTAMP_ADD",
    "TIMESTAMP_SUB",
    "TIMESTAMP_DIFF",
    "TIMESTAMP_TRUNC",
    "FORMAT_TIMESTAMP",
    "PARSE_TIMESTAMP",
    "TIMESTAMP_SECONDS",
    "TIMESTAMP_MILLIS",
    "TIMESTAMP_MICROS",
    "UNIX_SECONDS",
    "UNIX_MILLIS",
    "UNIX_MICROS",
    # Debugging functions
    "ERROR",
)

"""
Data Definition Language
https://cloud.google.com/spanner/docs/data-definition-language
"""
ddl = (
    "CREATE",
    "ALTER",
    "DROP",
    "DATABASE",
    "TABLE",
    "COLUMN"
    "PRIMARY",
    "INTERLEAVE",
    "PARENT",
    "ON",
    "OPTIONS",
    "INDEX",
    "UNIQUE",
    "NULL_FILTERED",
    "STORING",
    "ADD COLUMN",
)


class SpannerLexer(RegexLexer):
    """
    Special lexer for Spanner.
    http://pygments.org/docs/lexerdevelopment/
    """

    name = 'Spanner'
    aliases = ['spanner']
    mimetypes = ['text/x-spanner']

    flags = re.IGNORECASE

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'--.*\n?', Comment.Single),
            (r'/\*', Comment.Multiline, 'multiline-comments'),
            (words(syntax, suffix=r'\b'), Keyword),
            (words(keywords, suffix=r'\b'), Keyword),
            (words(datatypes, suffix=r'\b'), Name.Builtin),
            (words(functions, suffix=r'\b'), Name.Function),
            (words(ddl, suffix=r'\b'), Keyword),
            # Client commands
            (words(commands.keys(), suffix=r'\b'), Name.Builtin),
            (r'[+*/<>=~!@#%^&|`?-]', Operator),
            (r'\d+', Number.Integer),
            (r'(\d+\.\d*|\d*\.\d+)(e[+-]?[0-9]+)?', Number.Float),
            (r"'(''|[^'])*'", String.Single),
            (r'"(""|[^"])*"', String.Symbol),
            (r'[a-z_][\w]*', Name),
            (r'[;:()\[\],.]', Punctuation),
        ],
        'multiline-comments': [
            (r'/\*', Comment.Multiline, 'multiline-comments'),
            (r'\*/', Comment.Multiline, '#pop'),
            (r'[^/*]+', Comment.Multiline),
            (r'[/*]', Comment.Multiline)
        ],
    }

    # pylint: disable=no-self-argument
    def analyse_text(text) -> float:
        return 0.01

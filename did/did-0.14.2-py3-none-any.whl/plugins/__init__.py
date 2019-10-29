"""
Modules in this directory are searched for available stats. Each
plugin should contain a single class inheriting from StatsGroup.
Stats from this group will be included in the report if enabled in
user config. Name of the plugin should match config section type.
Attribute ``order`` defines the order in the final report.

This is the default plugin order:

    +----------+-----+
    | header   | 000 |
    +----------+-----+
    | google   | 050 |
    +----------+-----+
    | nitrate  | 100 |
    +----------+-----+
    | bugzilla | 200 |
    +----------+-----+
    | git      | 300 |
    +----------+-----+
    | github   | 330 |
    +----------+-----+
    | gerrit   | 350 |
    +----------+-----+
    | gitlab   | 380 |
    +----------+-----+
    | pagure   | 390 |
    +----------+-----+
    | trac     | 400 |
    +----------+-----+
    | trello   | 450 |
    +----------+-----+
    | rt       | 500 |
    +----------+-----+
    | redmine  | 550 |
    +----------+-----+
    | jira     | 600 |
    +----------+-----+
    | sentry   | 650 |
    +----------+-----+
    | wiki     | 700 |
    +----------+-----+
    | items    | 800 |
    +----------+-----+
    | footer   | 900 |
    +----------+-----+
"""

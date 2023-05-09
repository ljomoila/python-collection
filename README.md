# python-collection

Collection of small python application to help everyday life.

## Development

Make sure you have python 3 installed on your computer.

## on-call-developer

Generates weekly on-call-developer list to excel file for the year (or chosen weeks) with the backup developer.

List of developer names and weeks can be updated in `on-call-developer.py`

```
OnCallDeveloperList(['Lynx Lockwood', 'Rex Sharp', 'Nova Frost', 'Avery Steele',
                     'Phoenix Blaze', 'Raven Swift', 'Eliot Voss', 'Sage Harper'], 52).generate()
```

### RUN and Generate

- `pip install pandas` - installs pandas for xml creation
- `python3 on-call-developer/on_call_developer.py` - Runs application. As a result on-call-schedule.xlsx file is created.

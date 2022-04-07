1. Create virtual environment folder
```
python -m venv venv
```

2. Activate the virtual environment
```
source venv/bin/activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Add `.env` file

5. Run dev server
```
uvicorn main:app --host=0.0.0.0 --reload
```
The error `AttributeError: 'InfluxDBClient' object has no attribute 'api_client'` appears when Influx's env variables are not loaded correctly.

6. Update list of dependencies
```
pip freeze > requirements.txt
```

from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# Database Setup
# DATABASE_URI = "sqlite:///C:/Users/leors/Project-4-Credit-Worthiness/Resources/credit_worthiness.sqlite"
DATABASE_URI = "sqlite:///credit_worthiness.sqlite"
engine = create_engine(DATABASE_URI)


# Reflect the existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table (assuming you want to work with train_table)
TrainTable = Base.classes.TrainTable

# Flask Setup
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import requests
import random
import time
import pandas as pd
from datetime import datetime
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')


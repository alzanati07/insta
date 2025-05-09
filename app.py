from flask import Flask, render_template, request
import instaloader
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
L = instaloader.Instaloader()

proxy_user = os.getenv("PROXY_USER")
proxy_pass = os.getenv("PROXY_PASS")
proxy_host = os.getenv("PROXY_HOST")
proxy_port = os.getenv("PROXY_PORT")
proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

L.context.proxy = proxy_url

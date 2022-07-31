from diagrams import Diagram, Cluster
from diagrams.programming.framework import Angular, Fastapi
from diagrams.programming.language import NodeJS
from diagrams.onprem.database import PostgreSQL, MongoDB
from diagrams.onprem.client import User
from diagrams.onprem.queue import RabbitMQ

with Diagram("Planly Architecture Diagram", show=False, direction="LR"):
    user = User("Usuario")
    frontend = Angular("Nameless Frontend\nService")
    msg_broker = RabbitMQ("Message\nBroker")

    with Cluster("Main Services", direction="TB"):
        user_handler = Fastapi("Nameless User\nService")
        racoon = Fastapi("Racoon")

    with Cluster("Auxiliary Services"):
        chat_service = NodeJS("Nameless Chat\nService")
        AlSys = Fastapi("AlSys")
    
    with Cluster("Database\nCluster"):
        main_db = PostgreSQL("Main Database")
        side_db = MongoDB("Side Service\nDatabase")

    user >> frontend
    racoon - user_handler
    # main_db - side_db
    frontend >> racoon
    frontend >> user_handler

    racoon - msg_broker - user_handler
    
    racoon >> main_db
    user_handler >> main_db

    side_db - chat_service
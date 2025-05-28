# This is a test file for chat with sql project
from langchain.agents import * 
import os
from langchain.llms import openai
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

class ChatWithSQL:

    """ 
    This class is use for chat and query user question with the Sql database
    """

    def __init__(self, db_user, db_password, db_host, db_name):
        "This is an constructor method of the ChatWithSQL class"
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name

    def message(self, query):
        """
        "message" fuction will take the query from the user and process the result and return the response
        
        Args:
            query(string): This is the question of the user

        Return:
            response(string): This is the response generate by the llms
        """

        # Initializing the llms
        llm = ChatOpenAI(model_name = 'gpt-3.5-turbo')

        # Connecting with the database
        db = SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")

        # Initializing the Toolkit 
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        # Create the agent executer
        agent_executer = create_sql_agent(
            llm = llm,
            toolkit = toolkit,
            verbose=1
            )
        
        response = agent_executer.run(query)

        return response
    

obj = ChatWithSQL('root','madhu953','localhost','zomato')
print(obj.message("How many tables in this database?"))
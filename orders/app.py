from fastapi import FastAPI
#create an instance of fastapi class
#object represents our api application


app=FastAPI(debug=True)


# we import aour api module 

from orders.Api import api


#black
#pylance



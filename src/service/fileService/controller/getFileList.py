from flask import session
from flask_restful import Resource, reqparse
from params import params
from coreApis import coreApis
from utils import tokenValidator,sql
import requests
import logging
import json

param=params()
coreApi = coreApis()

class GetFileList(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('projectID',type=str,required=True)
        parser.add_argument('token',type=str,required=True)
        args = parser.parse_args()
        logging.debug(f"[GetFileList] args: {args}")

        projectID = args['projectID']

        #check user isLogin
        if tokenValidator(args['token']):
            
            resp = []
            try:
                db=sql()
                db.cursor.execute(f"select * from file where `project_id`='{projectID}'")
                result = db.cursor.fetchall()
                data=[list(a) for a in result]
                for item in data:
                    test: {
                        'test1': 'test1',
                        'test2': 'test2'
                    }
                    form = {
                        'fileUids': json.dumps(test),
                        'tokenstr': 'ab',
                        'tokenint': 293
                    }
                    logging.info(f'form:{form}')
                    response = requests.post( coreApi.GetFileStatus , data= form)
                    responseObj = response.json()
                    logging.info(f'result: {responseObj}')
                    if responseObj["status"] == 'success':
                        respItem = {
                            'fileID': item[0],
                            'fileName': item[2],
                            'fileStatus': responseObj["status"][0]
                        }
                        resp.append(respItem)
            except Exception as e:
                logging.error(str(e))
                db.conn.rollback()
            finally:
                db.conn.close()
            logging.debug(f"[GetFileList] resp: {resp}")
            return {"status":"success","msg":"","data":{'fileList': resp}},201


        else:
            return {"status":"error","msg":"user did not login","data":{}},401
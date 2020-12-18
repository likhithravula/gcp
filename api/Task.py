from flask_restful import Resource
import logging as logger

class Task(Resource):
    def get(self):
        logger.debug("Inside get call")
        return {
            {
                "platformJobs": [{
                "platformJobId": 1,
                "deploymentPublicId": "site1",
                "jobId": "8c23e664",
                "pluginName": "Clinical Application that processed the study",
                "patientHash": "13207e3d",
                "detectedDateTime": "2018-09-20T08:20:31.9250000+01:00",
                "dormantDateTime": "2018-09-20T08:20:33.9250000+01:00",
                "pluginStartDateTime": "2018-09-20T08:20:35.9250000+01:00",
                "pluginFinishedDateTime": "2018-09-20T08:20:36.9250000+01:00",
                "dicomObjectStoredInPacsDateTime": "2018-09-20T08:20:37.9250000+01:00",
                "numberOfStudies": 3,
                "numberOfRelevantStudies": 2,
                "numberOfSopsForPlugin": 5,
                "numberOfSopsEmitted": 1,
                "outcome": "<outcome>"
                }],
            total: 2
            }
        },200
    # def post(self):
    #     logger.debug("Inside post call")
    #     return {"status":"200","company":"QUANTIPHI","message" : "upload intern's data"},200
    # def put(self):
    #     logger.debug("Inside put call")
    #     return {"status":"200","company":"QUANTIPHI","message" : "put intern's data"},200
    # def delete(self):
    #     logger.debug("Inside delete call")
    #     return {"status":"200","company":"QUANTIPHI","message" : "delete intern's data"},200
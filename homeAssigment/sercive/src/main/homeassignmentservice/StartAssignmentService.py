from sercive.src.main.homeassignmentservice.impl.DevFileProp import DevFileProp
from sercive.src.main.homeassignmentservice.service.AssignmentService import AssignmentService


#dev application starter class ,flask sever start in localhost , port 4040
app=AssignmentService(DevFileProp()).initSrever()
app.run(host="0.0.0.0" ,port=5050)

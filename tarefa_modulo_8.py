from troposphere import Ref, Template
import troposphere.ec2 as ec2

t= Template()

instance = ec2.Instance('myinstance')
instance.ImageId = "ami-951945d0"
instance.InstanceTyoe = "t1.micro"
t.add_resource(instance)

instance2 = ec2.Instance('myinstance2')
instance2.ImageId = "ami-951945d0"
instance2.InstanceTyoe = "t1.micro"
t.add_resource(instance2)

instance3 = ec2.Instance('myinstance3')
instance3.ImageId = "ami-951945d0"
instance3.InstanceTyoe = "t1.micro"
t.add_resource(instance3)

print(t.to_json())

print(t.to_yaml())
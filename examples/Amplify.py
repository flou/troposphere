from troposphere import Template, Tags
from troposphere.amplify import App


template = Template()

app = template.add_resource(
    App(
        "App",
        Name="demo-application",
        Repository="https://github.com/acme/demo-app",
        Tags=Tags(Name="DemoApp"),
    )
)

print(template.to_json())

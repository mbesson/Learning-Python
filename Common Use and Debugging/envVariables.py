# Understanding environnement variables
# using the os module qith the function os.environ and os.getenv()
import os

#stage = os.environ['STAGE'].upper()
stage = os.getenv('STAGE','dev').upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "Danger!! - " + output

print(output)
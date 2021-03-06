import onebit
import os
import commands



cmd = '"$ANDROID_SDK"/"tools/android" list targets'
text = commands.getoutput(cmd)

if text == 'Available Android targets:':
    template = onebit.env.get_template("error.html")
    print template.render(
        title='Error',
        error='No build targets found.<br>Try installing some packages using the SDK & AVD Manager.'
    )
else:
    template = onebit.env.get_template("newproject.html")
    split = text.split("id: ")[1:]
    targets = []

    for s in split:
        parts = s.split("\n")
        if parts[3].strip()[-1:] != ".":
            api = parts[3].strip()[-1:]
        else:
            api = parts[6].strip()[-2:-1]
        targets.append({"id":parts[0][0], "label":"%s (%s)" % (parts[0].replace(" or ", ") "), parts[1].strip()[6:]), "api":api})

    print template.render(
        title='Create Android App', 
        targets=targets,
        homedir=os.environ['HOME'],
    )


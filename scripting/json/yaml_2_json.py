import sys, os, json, yaml


if len(sys.argv) > 1: # do we have more than 1 argument?
    if os.path.exists(sys.argv[1]): # is the filename passed actually present?
        yaml_string = yaml.safe_load(open(sys.argv[1]).read())

        # Convert dict to yaml
        json_string = json.dumps(yaml_string)

        # Check if the argument ends with .json
        if (sys.argv[2].endswith(".json")):

            # Checking if Yaml exists
            if not os.path.exists(sys.argv[2]):
            # Then create yaml and input yaml_string
                with open(sys.argv[2], "w") as json_file:
                    json_file.write(json_string)
                    print(f"Json file created: {sys.argv[2]}")
            else:
                # Checking if .json file exists
                print(f"{sys.argv[2]} exists, try again")
        else:
            print(f"{sys.argv[2]} not a valid .json name")
    else:
        # Checking for .yaml file
        print(sys.argv[1] + " not found")

else:
    print("Usage: python json_2_yaml.py <file.json> <file.yaml>")


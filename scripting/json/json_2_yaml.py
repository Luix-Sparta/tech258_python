import sys, os, json, yaml


if len(sys.argv) > 1: # do we have more than 1 argument?
    if os.path.exists(sys.argv[1]): # is the filename passed actually present?
        # Convert Json to dict
        json_string = json.loads(open(sys.argv[1]).read())

        # Convert dict to yaml
        yaml_string = yaml.dump(json_string)

        # Check if the argument ends with .yaml
        if (sys.argv[2].endswith(".yaml")):

            # Checking if Yaml exists
            if not os.path.exists(sys.argv[2]):
            # Then create yaml and input yaml_string
                with open(sys.argv[2], "w") as yaml_file:
                    yaml_file.write(yaml_string)
                    print(f"Yaml file created: {sys.argv[2]}")
            else:
                # Checking if .yaml file exists
                print(f"{sys.argv[2]} exists, try again")
        else:
            print(f"{sys.argv[2]} not a valid .yaml name")
    else:
        # Checking for .json file
        print(sys.argv[1] + " not found")

else:
    print("Usage: python json_2_yaml.py <file.json> <file.yaml>")


import bluetooth

target_name = "Pixel 7 Pro"
target_address = None
uuid = "38c8243b-d689-47a8-a5b3-f19fa41146c1"  # This should match the UUID on the Android server.

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

#for address, name in nearby_devices:
    #print("Name: {}, Address: {}".format(name, address))

# Find the address of your Pixel
for address, name in nearby_devices:
    print("Name: " + name + "| Address " + address + "| Target_Name " + target_name)
    if target_name == name:
        target_address = address
        print("Found Target Name in Nearby Devices - setting target_address ")
        break

if target_address is not None:
    service_matches = bluetooth.find_service(uuid=uuid, address=target_address)

    if len(service_matches) == 0:
        print("Couldn't find the service.")
        exit()

    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]

    # Connect to the server on the Pixel
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    print("Connecting to the server - Pixel Phone ")

    # Send the command
    sock.send("PLAY_TONE")
    sock.close()
    print("Sending PLAY_TONE command to the server - Pixel Phone ")

else:
    print("Could not find target device.")



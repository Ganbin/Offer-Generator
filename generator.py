import json
import subprocess

alias = "/Applications/Chia.app/Contents/Resources/app.asar.unpacked/daemon/chia"
outputPath = "./offers/"

with open("data.json") as file:
    data = json.load(file)
    offerAmount = data["requestAmount"] / data["price"] / data["nbTogenerate"]
    requestAmount = round((data["requestAmount"] / data["nbTogenerate"]), 4)
    increment = 1 + ((data["increment"] / data["nbTogenerate"]) / 100)
    fingerprint = data["walletFingerprint"]

    for i in range(1, data["nbTogenerate"] + 1):
        fileName = outputPath + str(i) + ".offer"
        command = [
            alias,
            "wallet",
            "make_offer",
            "-f",
            fingerprint,
            "-o",
            str(data["offerWalletID"]) + ":" + str(round(offerAmount, 4)),
            "-r",
            str(data["requestWalletID"]) + ":" + str(requestAmount),
            "-p",
            fileName,
        ]
        subprocess.run(command, text=True, input="y")
        offerAmount = offerAmount / increment  # Increment the price each offer

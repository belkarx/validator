comp = input("What is your complaint: ").replace("'", "").replace("\"", "")
void = input("Do you want other people to be able to commiserate with this (y/n): ")
if "y" in void:
    void = "True"
else:
    void = "False"
val = input("Do you want to be validated by an AI (y/n): ")
if "y" in val:
    val = "True"
else:
    val = "False"


print("curl -X POST -H \"Content-Type: application/json\" / -d '{" + f"\"complaint\":\"{comp}\", \"validate\": \"{val}\", \"into_void\": \"{void}\"" + "}' / http://127.0.0.1:8000/complain""")


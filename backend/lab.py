
import subprocess

cmd = ["diff", "-B", "-w", "out.txt", "recive.txt"]

ans = subprocess.run(cmd, timeout=10,check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(ans.returncode)
print(ans.stdout)
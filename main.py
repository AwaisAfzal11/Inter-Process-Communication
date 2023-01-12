import subprocess


buffer = "name first"
# Open a pipe to the 'wc' command with the '-c' option
# using the 'subprocess.Popen' function
with subprocess.Popen(["find","/c"],stdin=subprocess.PIPE,stdout=subprocess.PIPE) as process:
    # Write the contents of 'buffer' to the pipe
    # using the 'stdin' attribute of the Popen object
    process.stdin.write(buffer.encode())
    process.stdin.close()

    # Read the output of the 'wc' command
    # using the 'stdout' attribute of the Popen object
    output = process.stdout.read()
    print(output.decode())
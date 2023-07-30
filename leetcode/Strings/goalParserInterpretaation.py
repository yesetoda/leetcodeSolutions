class Solution:
    def interpret(command: str) -> str:
        if "(al)" in command:
            command = command.replace("(al)","al")
        if "()" in command:
            command = command.replace("()","o")
        if "G" in command:
            command = command.replace("()","G")
        return command
    command = "G()()()()(al)"
    print(interpret(command))
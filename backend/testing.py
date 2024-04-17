from TheatreChatBot import TheatreChatBot

tc = TheatreChatBot("kochi")

result = tc.execute_result("available movies and their time")

print(result)
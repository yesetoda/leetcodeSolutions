class Solution:
    def asteroidCollision(asteroids: list[int]) -> list[int]:
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                print(stack)
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
    print(asteroidCollision(asteroids = [10,2,-5]))
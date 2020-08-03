#!/usr/bin/env python
# coding: utf-8

# # N면체 주사위 만들기

# In[1]:


# Library
from random import randrange


# In[2]:


class FunnyDice:
    def __init__(self,n=6): # default를 6으로 지정
        self.n = int(n)
        self.numbers = list(range(1,n+1)) # 주사위 숫자를 list에 넣기
        self.index = randrange(0,self.n) # random index 뽑아내기
        self.val = self.numbers[self.index] # random index 자리의 숫자 뽑아내기
        
    # random하게 주사위 눈 나오게 함.
    def throw(self):
        self.index=randrange(0,self.n)
        self.val=self.numbers[self.index]
    
    # random으로 뽑은 인덱스 자리의 주사위 값
    def getval(self):
        return self.val
    
    def setval(self, val:int):
        if val <= self.n:
            self.val=val
        else:
            print("주사위에 없는 숫자입니다. 주사위는 1 ~ {0}까지 있습니다.".format(self.n))
            raise error


# In[3]:


def get_inputs():
    n = int(input("주사위 면의 개수를 입력하세요:"))
    return n


# In[4]:


def main():
    # 주사위 면의 수 입력 받음
    n = get_inputs()
    # FunnyDice라는 클래스로부터 mydice를 인스턴스 객체로 만들기
    mydice = FunnyDice(n)
    mydice.throw()
    print("행운의 숫자는?{}".format(mydice.getval()))
    


# In[6]:


if __name__=='__main__':
    main()


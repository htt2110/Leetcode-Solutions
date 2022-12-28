#include<iostream>
#include<string>

bool isPalindrome(int x) {
        std::string s = std::to_string(x);
        int l = s.length();
        int end = l-1;
        for(int i = 0; i < l; i++){
            if(s[i] != s[end - i])
                return false;
        };
        return true;
    } 

int main(){
    int x = 121;
    std::cout << isPalindrome(x) << std::endl;
    return 0;
}
#include<iostream>
#include<vector>
#include<map>

std::vector<int> twoSum(std::vector<int> nums, int target) {
    std::map<int, int> required;
    std::vector<int> out;
    for(int i = 0; i <nums.size(); i++){
        if(required.find(target-nums[i]) != required.end()){
            out.push_back(required[target-nums[i]]);
            out.push_back(i);
            return out;
        }
        else{
            required[nums[i]] = i;
        }
    }
return out;
}

int main(){
    int target = 9;
    std::vector<int> nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);
    
    std::vector<int> out = twoSum(nums, target);
    for(int i = 0; i<out.size(); i++){
        std::cout << out[i] <<" ";

    }
    return 0;
}
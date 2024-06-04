#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;

    // 입력 벡터가 비어있는지 확인
    if(arr.empty()) {
        return answer;
    }

    answer.push_back(arr[0]);

    for(int i = 1; i < arr.size(); i++) {
        if(answer.back() == arr[i])
            continue;

        answer.push_back(arr[i]);
    }
    return answer;
}
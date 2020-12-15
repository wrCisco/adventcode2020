#include <array>
#include <string>
#include <fstream>
#include <iostream>

int main()
{
  std::ifstream in { "input.txt" };
  std::string input { std::istreambuf_iterator<char> {in}, std::istreambuf_iterator<char>{}};
  std::array<int, 7> nums;
  std::size_t pos = 0, proc = 0;
  int i = 0;
  while (pos < input.size()) {
    nums[i++] = std::stoi(input.substr(pos), &proc);
    pos += proc + 1;
  }
  auto *prevs = new std::array<int, 30000000>{};
  for (int i = 1; i <= nums.size(); ++i) {
    (*prevs)[nums[i-1]] = i;
  }
  int last = nums.back();
  for (int turn = nums.size(); turn < 30000000; ++turn) {
    int n = (*prevs)[last] ? turn - (*prevs)[last] : 0;
    (*prevs)[last] = turn;
    last = n;
    if (turn == 2019) {
      std::cout << last << '\n';  // first answer
    }
  }
  std::cout << last << '\n';  // second answer
  return 0;
}

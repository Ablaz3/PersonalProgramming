// template arguments
#include <iostream>
using namespace std;

template <class T, class N>
T fixed_multiply (T val, N val2)
{
  return val * val2;
}

int main() {
  std::cout << fixed_multiply<int,int>(10, 2) << '\n';
  std::cout << fixed_multiply<int,int>(10, 3) << '\n';
}
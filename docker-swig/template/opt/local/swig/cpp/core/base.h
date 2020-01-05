#pragma once

namespace core {
  int fact(int n);

  class Base {
  //private typedef
  private:
  //public typedef
  public:
  //public function
  public:
    Base(const int value): value_(value) {
    }

    int PublicMethod(const int value);
  //private function
  private:
  //private members
  private:
    int value_;
  };
} // namespace ns1


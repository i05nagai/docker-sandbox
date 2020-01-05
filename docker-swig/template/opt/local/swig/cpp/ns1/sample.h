#pragma once
#include "core/base.h"

namespace ns1 {
  int fact(int n);

  class Derived: public core::Base {
  //private typedef
  private:
  //public typedef
  public:
  //public function
  public:
    Derived(const int value): Base(value) {
    }

    int PublicMethod(const int value);
  //private function
  private:
  //private members
  private:
    int value_;
  };
} // namespace ns1

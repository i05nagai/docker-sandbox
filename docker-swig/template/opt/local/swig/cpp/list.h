#pragma once
#include <iostream>

// Very simple C++ example for linked list
class List {
public:
  List();
  ~List();
  int search(char* value);
  void insert(char* value);
  void remove(char* value);
  char get(int n);
  static void print(List *l) {
    for (int i = 0; i < l->length; ++i) {
      std::cout << l->get(i) << ", ";
      std::cout << std::endl;
    }
  }
  int length;
private:
  int size_;
  char* data_;
};

List* new_list(void);
void delete_list(List *l);

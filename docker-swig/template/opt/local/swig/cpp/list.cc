#include "list.h"
#include <stdlib.h>

List::List() {
  this->length = 0;
  this->size_ = 8;
  this->data_ = (char *)malloc(length * sizeof(char));
}

List::~List() {
  delete(this->data_);
}

int List::search(char *value) {
  for (int i = 0; i < this->length; ++i) {
    if (this->data_[i] == *value) {
      return i;
    }
  }
  // not found
  return -1;
}

void List::insert(char* value) {
  if (length >= size_) {
    this->size_ *= 2;
    this->data_ = (char *)realloc(this->data_, this->size_ * sizeof(char));
  }
  this->data_[this->length] = *value;
  this->length++;
}

void List::remove(char* value) {
  const int index = this->search(value);
  if (index != -1) {
    for (int i = index; i < this->length - 1; ++i) {
      this->data_[i] = this->data_[i + 1];
    }
    this->length--;
  }
}

char List::get(int n) {
  return this->data_[n];
}

List * new_list(void) {
  return new List;
}

void delete_list(List *l) {
  delete l;
}

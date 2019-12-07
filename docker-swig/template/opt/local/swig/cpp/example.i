%module example
%{
#include "list.h"
#include "sample.h"
#include "foo.h"
%}
%include "list.h"
%include "foo.h"
%include "sample.h"

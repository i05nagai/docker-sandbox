%module ns1
%{
#include "../core/base.h"
#include "sample.h"
%}

%ignore core::fact(int n);
%include "../core/base.h"

%include "sample.h"


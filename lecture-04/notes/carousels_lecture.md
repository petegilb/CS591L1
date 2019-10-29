```neptune[inject=true,language=CSS]
body {
  padding-right: 20%;
  padding-left: 20%;
  line-height: 1.6;
  font-family: Verdana,Arial,Sans-serif;
  color:#173834;
}

h1 {
  color:#C48C17;
  font-weight: light;
  padding-bottom: 3%;
}

h2 {
  padding-top: 2%;
  padding-bottom: 1%;
  color:#C48C17;
  font-weight: light;
}
```

```neptune[inject=true,language=javascript]
function getEditor(id) {
  return document.getElementById(id).getElementsByClassName('code-mirror-div')[0].codeMirrorInstance;
}

window.addEventListener('load', function() {
  var codeMirrorInstance = getEditor('carousels1-tab-2-tab');
  var metrics = JSON.stringify(costs["onlineRounds"], null, '  ');
  codeMirrorInstance.setValue(metrics);
  codeMirrorInstance.refresh();
});

function getSampleCode() {
  return getEditor('sample-tab-1-tab').getValue();
}

function getTransformationCode() {
  return getEditor('transform-tab-2-tab').getValue();
}

function setTransformationCode(code) {
  var codeMirrorInstance = getEditor('transform-tab-2-tab');
  codeMirrorInstance.setValue(code);
  codeMirrorInstance.refresh();
}

function getCarouselsCode() {
  return getEditor('carousels1-tab-1-tab').getValue();
}

function getCosts() {
  return JSON.parse(getEditor('carousels1-tab-2-tab').getValue());
}
```

# Babel

Babel is a Javascript compiler and parse. Babel exposes the AST of input code to developers, and
allows them to write their own custom transformations to modify the AST/code.

Babel comes with built in transformations, for example, converting new JS syntax and features
(e.g. ES6+) into backward compatible JS supported by older environments. *In practice,
you may often use JS features that will not be supported by your clients browsers
(e.g. Internet Explorer) and would need such a tool.* You can test this transformation out and play
around with a dummy example over
[here](https://babeljs.io/repl/#?babili=false&browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=NoRgNABATJDMC6A6AtgQwA4ApMDsCUEAvAHwQ4QDUEIeAUEA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=es2015%2Creact%2Cstage-2&prettier=false&targets=&version=7.6.0&externalPlugins=).

Here is a [list](https://github.com/babel/awesome-babel) of many different projects that use
Babel to implement interesting things!

Babel's compilation process happens in 3 steps:
1. Generate an AST by parsing the JS code.
2. Transform the AST in order to transpile the code into older versions of JS.
3. Generate the resulting code from the transformed AST.

## First Babel Example

As a first example, we will use Babel to transform a piece of code that uses the new
ES6 style functions (defined using =>). The output code will replace all such function
definitions with old-style function definition.

Below is the example code we would like to transform.

```neptune[title=Sample&nbsp;Code,language=javascript,scope=none,frame=sample]
var addTwo = x => x + 2;
Console.log(addTwo(1));
```

Fortunately, Babel implements this transformation using a built-in babel plugin: **transform-es2015-arrow-functions**.
This plugin implements the syntax transformation logic, and runs during the second step of Babel's compilation
process above.

The code below demonstrates how it can be used to perform the transformation.


```neptune[title=Sample&nbsp;Transformation,language=javascript,scope=sample]
// Get the code from the panel above
var code = getSampleCode();
Console.log('input code: ------------');
Console.log(code.trim());
Console.log('------------------------');
Console.log('');

// Apply the transformation plugin on the input code's AST: notice that several plugins can be applied
var result = Babel.transform(code, {plugins: ['transform-es2015-arrow-functions']});
Console.log('output code: --------------');
// result contains many properties resulting from transformation, including the new code
Console.log(result.code);
Console.log('---------------------------');
```
## Code Transformation with Babel

The above example was very simple, because the transformation was already built by Babel. However,
in many cases, the desired transformation is not implemented, and we must implement it ourselves.

We will start with a simple code transformation: we want to write a code transformation that will
replace every + operation with a - operation instead.

Custom transformation plugins in Babel must implement a visitor pattern. Babel will use that
visitor pattern to apply this desired transformation. This operates as a tree traversal over the AST.
Babel starts from the root of the AST, and recurses by visting all children of the root in order.

Every time babel reaches a node (including the root), it determines its type (e.g. function definition, binary
expression, etc), and then calls the **enter** function for that type, as provided by the visitor pattern, Babel passes
the current node as a parameter to the function. When babel finishes traversing all children of a node, it
calls the **exit** function for that node's type, and backtracks to its parent node, repeating the same procedure.

Therefore, The visitor pattern is parameterized both the stage of the function (enter or exit) and the type of the node
being visited. Babel supports visitor patterns including any combination of stage and node types, with the unprovided functions
or types set to some default.

Visitor patterns are a common design pattern in many languages, follow these links to read more about the
[Babel plugins & visitor patterns](https://medium.com/the-guild/this-is-how-i-build-babel-plug-ins-b0a13dcd0352) and
[visitor patterns](https://www.geeksforgeeks.org/visitor-design-pattern/) in object oriented programming in general.

Here is a very simple visitor pattern that implements our desired transformation. The pattern
only looks at binary expressions, since we are only concered with +. **Please Run These code tabs in order.**

```neptune[title=Visitor&nbsp;Pattern,language=javascript,scope=transform,frame=transform]
var visitorPattern = {
  visitor: {
    BinaryExpression: {
      exit: function (path, state) {
        if (path.node.operator === '+') {
          path.node.operator = '-';
        }
      }
    }
  }
};
Console.log('Visitor pattern defined!');
```

Here is a sample program we would like to transform.
```neptune[title=Sample&nbsp;Code,language=javascript,scope=none,frame=transform]
var x = 10 + 2;
var y = (x * 2) + 4;
Console.log('(10 + 2) * 2 + 4 =', y);
```

Finally, we can put all these pieces together, by telling Babel to use our visitor
pattern, and transform the code with it!
```neptune[title=Sample&nbsp;Transformation,language=javascript,scope=transform,frame=transform]
// Get the code from the sample code tab
var code = getTransformationCode();
Console.log('input code: ------------');
Console.log(code.trim());
Console.log('------------------------');
Console.log('');

Babel.registerPlugin('my-transformation', function () {
  return visitorPattern; // variable from first tab
});

var result = Babel.transform(code, {plugins: ['my-transformation']});

Console.log('output code: --------------');
Console.log(result.code);
Console.log('---------------------------');
eval(result.code);

setTransformationCode(result.code);
```
&nbsp; 

&nbsp; 

# Static Cost Analysis: Carousels

These notes cover an example of defining and analyzing abstract metrics over
[jiff](https://multiparty.org/jiff/docs/jsdoc/), a generic Javascript framework
for MultiParty Computation (MPC).

*Relevant libraries: [jiff](https://multiparty.org/jiff/docs/jsdoc/),
[Babel](https://babeljs.io/),
[polynomium](https://github.com/lapets/polynomium/),
[imparse](https://github.com/lapets/imparse),
and [plotly](https://plot.ly/javascript/)*

*You can also find the full working version of carousels [here](https://multiparty.org/carousels/)
and the [source code here](https://github.com/multiparty/carousels)*.

## Introduction

It is often critical in practice to automatically give upper bounds and
estimates on resource usage of programs before reaching production.
Several such scenarios include:

  * Safety critical applications where we may need to catch vulnerabilities and side channels before deployment.
  * Time critical applications where we need to finish tasks in a hard deadline.
  * Memory critical applications where we may be limited by the total amount of memory our program can use.
  * Cost critical applications where there may be a $ cost per resource usage.
  * etc.

This problem is somewhat juxtaposed to the problem of giving asymptotic bounds of *whatever
metric you pick* for algorithms because of the importance of giving representative constants:
While in an algorithms course you may be told that binary search takes in the worst case O(1) space complexity, we will
actually care about the hidden constant that is slipped under the Big Oh notation.
That will sometimes make the difference between saying that our program will use
10 GB or 10 MB in memory.

While it may generally be undecidable to perform resource estimates of generic programs,
we may restrict our focus on subsets of languages for which the problem becomes solvable.
Fortunately, these restrictions do not completely deter our programs expressiveness and may
still form meaningful estimates for codes that programmers typically develop.

## Problem Definition

In our specific example, we will be looking at the problem of estimating relevant metrics for
MPC *(a subfield of cryptography that deals with distributive protocols for computing functions
over secret data among multiple parties)*: the numbers of rounds of communication an MPC protocol
takes.

We need to do so by never actually running the program but rather statically analyzing it.
In order to do so, we will be:

1. Specifying the costs of MPC primitives written in jiff. These costs may later be updated
depending on the environment in which we run our protocol *(browser, hardware, etc.)*.
2. Parsing the code we would like to analyze according to Javascripts grammar and transforming
it into an AST. Thankfully for us, Babel will take care of tokenizing and annotating different
sections of the code and will produce the necessary AST for us.
3. Traversing the AST and deriving our metric. We do so by exposing Babel's visitor patterns
and cumulatively constructing the metric accordingly.
4. Plotting our findings for visualization and interpretation of results.

## Carousels

We will specifically be using Babel's plugins. These plugins are executed in the
2nd compilation step and allow for custom or predefined transformations of the AST.
Without any plugins, Babel will not modify the AST.

We will register a `metric` plugin that will inject a `metric` parameter in each node of the AST,
then define how to construct this metric in the visitor patterns. The idea is that as we exit a node
in the AST (for example: a binary expression), we check what kind of node and operation we visited,
and match it to the cost specifications. We also accumulate all costs from the node's children,
and pass the aggregated cost to the node's parent.

**Please run these code tabs in order!**

```neptune[title=Code&nbsp;to&nbsp;Analyze,language=javascript,frame=carousels1,scope=none]
function demo(x) {
  var arr = [1,2,3,4];

  var arr_bool = arr.map((curr, i) => arr[i].lt(arr[i+1]));
  arr = arr.map((curr,i) => arr_bool[i].if_else(arr_bool[i-1].if_else(arr[i],arr[i-1]), arr[i+1]));

  return arr;
}
```

```neptune[title=Cost&nbsp;specification,language=javascript,frame=carousels1,scope=none]

```


```neptune[title=Cost&nbsp;Analysis,language=javascript,outputID=myPlot,frame=carousels1,scope=carousels1]
var code = getCarouselsCode(); // gets the code from the panel above
var costs = getCosts(); // gets the cost specifications from the panel above

// Turn each of the cost specification into a polynomial object that can be manipulated
for (var op in costs) {
  costs[op] = carousels.parsePoly(costs[op]);
}

// Register the 'metric' plugin and specificy the method which construct the
// metric (i.e. "createMetric").
Babel.registerPlugin('metric', createMetric(costs));

// Apply the metric on the input code's AST
var bbl = Babel.transform(code, {plugins: ['metric']});

// Retrieve the result of the transformation
var bbl_result = bbl.ast.program.results;
Console.log('babel result:', JSON.stringify(bbl_result, {maxLength:120}).trim());

// The output of Babel returns a string. We use the polynomium library to turn
// this string into an actual polynomial.
var pol = carousels.parsePoly(bbl_result['demo']);
Console.log('Poylnomial:', pol);

// Compute the polynomial over actual inputs (compute_values invoke polynomium's
// method for evaluating polynomials on inputs)
var results = compute_values([pol], 1);

// Plot the results
plot2d('onlineRounds', 'bubblesort', results);
```


## Carousel's Metric Plugin Visitor Patterns

Below is a slightely deeper look at the implementation of carousels metric plugin.
This is a simplified portion of the visitor pattern, it does not include all the AST node
types and all the constructs that carousels support, only a minimal set of constructs
sufficient to have some understanding of the implementation.

Generally, visitor patterns for code analysis or transformation contains a small subset
of AST node types that are transformed or analyzed (e.g. BinaryExpression below), along
side a large subset of node types that do not have interesting manipulation, but are only
used to accumulate or propagate the result of analysis or transformation from their children
to their parent node (up to the AST root).

```neptune[title=Visitor&nbsp;Pattern,language=javascript,scope=none]
var zeroPolynomial = polynomium.c(0).toObject(); // create constant polynomium = 0
var plusPolynomial = function (sum, node) { return polynomium.add(sum, node.metric).toObject(); };

var visitorPattern = {
  visitor: {
    // root note in AST:
    // go every every function definition, and store the resulting cost polynomial for every function
    Program: {
      "exit": function (p) {
        var results = {}, metric = {};
        for (var i = 0; i < p.node.body.length; i++) {
          metric[p.node.body[i].id.name] = p.node.body[i].metric;
          results[p.node.body[i].id.name] = polynomium.toString(p.node.body[i].metric);
        }
        p.node.metric = metric;
        p.node.results = results;
      }
    },
    // Binary expression: look up operator in cost specifications and use that cost
    BinaryExpression: {
      "exit": function (p) {
        var start = p.node.loc.start, op = p.node.operator;
        if (op in costs) {
          p.node.metric = [p.node.left, p.node.right].reduce(plusPolynomial, costs[op]);
        } else {
          throw Error("Node type BinaryExpression with operator " + op +
                      " is not handled at line " + start.line + ", column " + start.column + ".");
        }
      }
    },
    // Propagate cost from the children of each of these nodes up
    FunctionDeclaration: {
      "exit": function (p) { p.node.metric = p.node.body.metric; }
    },
    BlockStatement: { // a block statement's cost is the sum of the cost of all its content
      "exit": function (p) { p.node.metric = p.node.body.reduce(plusPolynomial, zeroPolynomial); }
    },
    Identifier: {
      "exit": function (p) { p.node.metric = zeroPolynomial; }
    },
    VariableDeclaration: {
      "exit": function (p) { p.node.metric = p.node.declarations.reduce(plusPolynomial, zeroPolynomial); }
    },
    VariableDeclarator: {
      "exit": function (p) { p.node.metric = p.node.init.metric; }
    },
    ReturnStatement: {
      "exit": function (p) { p.node.metric = p.node.argument.metric; }
    },
    NumericLiteral: {
      "exit": function (p) { p.node.metric = zeroPolynomial; }
    }
  }
};
```


## Future Work

We are working on extending Carousels to other languages and to support other MPC frameworks, we want
to support more language features such as for loops, and support user-defined dimensions.

## Contact

If you have any questions feel free to ask me on Piazza or email me at ra1issa@bu.edu

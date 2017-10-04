title: Embracing Limits as a (Functional) Programmer

<header id="article-header" markdown="1">
Thoughts on
[Why Programmers Need Limits](https://medium.com/@cscalfani/why-programmers-need-limits-3d96e1a0a6db){target="_blank"}
by Charles Scalfani.
</header>

Charles makes an argument that as programmers we need to embrace limitations in a field where nearly anything is possible.

With great power comes great responsibility and often times software issues arise precisely out of programmers
*mishandling* a language's powerful capabilities *(global mutable state, anyone?)*.
  
> It’s the lack of limits that makes writing and maintaining software so difficult.

Functional languages in particular provide certain limitations
that ultimately encourage better coding practices *(e.g. immutability)*.

As programmers we need to learn from common pitfalls and set *(and embrace!)* limits
to keep ourselves from running into similar problems in the future.

The *[GOTO](https://en.wikipedia.org/wiki/Goto)* statement
is a classic example of a limitation imposed on programmers *(by programmers!)* for a greater good.

Though powerful, the hard-to-follow *Spaghetti code* that often resulted from GOTO's use
led to it being banned from most languages for the sake of code readability.

> What the progressive minds realized is that **code is read more than it’s written or changed**.
> So it may be a little less convenient for a small group of feet-draggers
> but in the long run we’d be far better off with this limitation.   

> Computers can still do *GOTO*s. In fact, they need to.
> It’s just that we, as an industry, decided to limit programmers from **directly** using them.
> All computer languages compile to code that uses *GOTO*s.
> But language designers created constructs that employed more disciplined branching,
> e.g. using a *break* statement to exit a *for* loop.

Charles highlights common problems programmers currently face
*(i.e. the **GOTOs of today**)* and what solutions are offered by functional languages:

> - Complexity
> - Reusability
> - Global Mutable State
> - Dynamic Typing
> - Testing
> - The Demise of Moore's Law

#### Complexity

Writing code that is decomposed helps reduce the inevitable complexity that occurs as programs grow over time.

Functional languages encourages decomposing a problem into a collection of manageable self-contained functions.

> Limiting programmers to only pure functions greatly limits complexity since
> functions can only have a local effect and helps developers naturally decompose their solutions.

#### Reusability

Developers often rely on copy/paste/modify *(though few will admit it!)*
when coding similar bits of functionality.

Functional languages have constructs that make reusing code easier and more practical
*(e.g. Higher-order Functions, Currying, Function Composition)*.

> ... while we cannot eliminate copypasta, we can make it unnecessary through language support ...

#### Global Mutable State

Mutable state makes it harder to reason about and debug programs.

Functional languages encourage the use of immutable variables to avoid mutability issues altogether.

> Proper management of state is the most important thing you can do in your program to ensure reliability.
> Functional Programming solves this problem by placing limits on programmers at the language level.
> Programmers cannot create mutable variables.

> ... when side-effects must happen, Functional Languages have ways of containing potentially dangerous parts of your program.
> ... these parts of the code are clearly marked as dangerous and segregated from the pure code.
> This gives the programmer a fighting chance to find [and fix] ... bugs since the dangerous parts are corralled.

#### Dynamic Typing

Static and Dynamic Typing both have their advantages and disadvantages.

Static Typing can be too verbose while Dynamic Typing can increase the likelihood of runtime errors.

Functional languages typically support *Type Inference* which gives the best of both.

> Many Functional Programming languages support *Type Inference*
> where the compiler can infer the types of functions you’re writing by the way you use them.
> This means we can have Static Typing without all of the overhead of specifying.

> So by limiting programmers to good Static Typing, the compiler can actually help detect bugs, infer types
> and aid in coding instead of burdening the developer with verbose, intrusive, type information.

#### Testing

Testing can be hard and time consuming.

Functional language encourage the use of pure functions, which are easier to test because they are
self-contained units with no side-effects and always produce the same result for the same input.
    
> ... if we limit the code to be Pure Functions, then
> ... [we'll] have our dangerous code layer as a very thin interface layer leaving the majority of the module as pure
> ... [. And] testing pure functions is far easier.

#### The Demise of Moore’s Law

Current CPU technologies are reaching a performance limit
and the best way to increase speed is to use more cores.

To utilize more cores, programs need to be sliced into parallel parts, which is not an easy task.

Functional languages encourage the use of immutability and pure functions,
which make it easier to write and execute parallel code.

> ... with Pure Functions, it doesn't matter what order they are run.
> All that matters is that the inputs are available.
> This means that the compiler or runtime system can determine which functions to run and when.

> By limiting functions to pure functions, it frees the programmer up from having to worry about parallelism.

#### Conclusion

Embrace the limitations imposed by functional languages.

Understand why the limitations are needed.

There's a reason why they're there.



<footer id="article-footer" markdown="1">
**P.S.**
The idea that **limitations can be good** is nothing new and not just related to programming...   

- [The Paradox of Choice - Why More Is Less](https://en.wikipedia.org/wiki/The_Paradox_of_Choice){target="_blank"} by Barry Schwartz
    ([video](https://www.youtube.com/watch?v=VO6XEQIsCoM){target="_blank"})
- [Embrace Constraints](https://gettingreal.37signals.com/ch03_Embrace_Constraints.php){target="_blank"} by 37signals
</footer>

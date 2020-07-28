# Signals-and-some-manipulations

## Introduction: 

Let's assume we are given a signal x(t), continuous and differentiable.

<em>exempli gratia</em> :

<img src="https://i.upmath.me/svg/x(t)%20%3D%20sin(t)" alt="x(t) = sin(t)" />

Now, regarding a practical analysis we can't generate a signal such that we get infinite precision. Thus, to address the signals in real life we can use sampling methods that shall render our signal in a very good approximation. Such a method will convert our signal from a continuous domain to a discrete one.

Also let us define a sampling interval T, and we will get a discrete signal x. Formulated as:

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20x(nT)" alt="x[n] = x(nT)" />

Sampling Example:

In signal processing some tools are introduced for various reasons and to assist in different scenarios. Some of which are: Upsampling, Downsampling, Interpolating and Decimating.

Their definitions are given as:

#### Upsampling: 

<img src="https://i.upmath.me/svg/x_i%5Bn%5D%20%3D%20x(nT%2FL)" alt="x_i[n] = x(nT/L)" />

#### Downsampling:

<img src="https://i.upmath.me/svg/x_d%5Bn%5D%20%3D%20x(nMT)" alt="x_d[n] = x(nMT)" />

#### Interpolating: 

We design a system using upsampling, such is given as:

<img src="https://i.upmath.me/svg/%5Cusetikzlibrary%7Barrows%7D%0A%5Cbegin%7Bdocument%7D%0A%5Cpagestyle%7Bempty%7D%0A%5Ctikzstyle%7Bint%7D%3D%5Bdraw%2C%20fill%3Dgray!8%2C%20minimum%20size%3D5em%5D%0A%5Ctikzstyle%7Binit%7D%20%3D%20%5Bedge%3D%7Bto-%2Cthin%2Cblack%7D%5D%0A%5Cbegin%7Btikzpicture%7D%5Bnode%20distance%3D5.5cm%2Cauto%2C%3E%3Dlatex'%5D%0A%20%20%20%20%5Cnode%20%5Bint%5D%20(a)%20%7B%24%5Cuparrow%20L%24%7D%3B%0A%20%20%20%20%5Cnode%20(b)%20%5Bleft%20of%3Da%2Cnode%20distance%3D4cm%2C%20coordinate%5D%20%7Ba%7D%3B%0A%20%20%20%20%5Cnode%20%5Bint%5D%20(c)%20%5Bright%20of%3Da%5D%20%7B%24%5Cbegin%7Bgathered%7D%5Ctext%7BL.P.F.%7D%5C%5C%20Gain%3DL%5C%5C%5Comega_%7Bco%7D%3D%5Cpi%2FL%5Cend%7Bgathered%7D%24%7D%3B%0A%20%20%20%20%5Cnode%20%5Bcoordinate%5D%20(end)%20%5Bright%20of%3Dc%2C%20node%20distance%3D4.5cm%5D%7B%7D%3B%0A%20%20%20%20%5Cpath%5B-%3E%5D%20(b)%20edge%20node%20%7B%24x%5Bn%5D%24%7D%20(a)%3B%0A%20%20%20%20%5Cpath%5B-%3E%5D%20(a)%20edge%20node%20%7B%24x_e%5Bn%5D%24%7D%20(c)%3B%0A%20%20%20%20%5Cdraw%5B-%3E%5D%20(c)%20edge%20node%20%7B%24x_i%5Bn%5D%24%7D%20(end)%3B%0A%5Cend%7Btikzpicture%7D%0A%5Cend%7Bdocument%7D%0A" alt="\usetikzlibrary{arrows}
\begin{document}
\pagestyle{empty}
\tikzstyle{int}=[draw, fill=gray!8, minimum size=5em]
\tikzstyle{init} = [edge={to-,thin,black}]
\begin{tikzpicture}[node distance=5.5cm,auto,&gt;=latex']
    \node [int] (a) {$\uparrow L$};
    \node (b) [left of=a,node distance=4cm, coordinate] {a};
    \node [int] (c) [right of=a] {$\begin{gathered}\text{L.P.F.}\\ Gain=L\\\omega_{co}=\pi/L\end{gathered}$};
    \node [coordinate] (end) [right of=c, node distance=4.5cm]{};
    \path[-&gt;] (b) edge node {$x[n]$} (a);
    \path[-&gt;] (a) edge node {$x_e[n]$} (c);
    \draw[-&gt;] (c) edge node {$x_i[n]$} (end);
\end{tikzpicture}
\end{document}
" />

#### Decimating:

We design a system using downsampling, given by:

<img src="https://i.upmath.me/svg/%5Cusetikzlibrary%7Barrows%7D%0A%5Cbegin%7Bdocument%7D%0A%5Cpagestyle%7Bempty%7D%0A%5Ctikzstyle%7Bint%7D%3D%5Bdraw%2C%20fill%3Dgray!8%2C%20minimum%20size%3D5em%5D%0A%5Ctikzstyle%7Binit%7D%20%3D%20%5Bedge%3D%7Bto-%2Cthin%2Cblack%7D%5D%0A%5Cbegin%7Btikzpicture%7D%5Bnode%20distance%3D5.5cm%2Cauto%2C%3E%3Dlatex'%5D%0A%20%20%20%20%5Cnode%20%5Bint%5D%20(a)%20%7B%24%5Cbegin%7Bgathered%7D%5Ctext%7BL.P.F.%7D%5C%5C%20Gain%3D1%5C%5C%5Comega_%7Bco%7D%3D%5Cpi%2FM%5Cend%7Bgathered%7D%24%7D%3B%0A%20%20%20%20%5Cnode%20(b)%20%5Bleft%20of%3Da%2Cnode%20distance%3D4cm%2C%20coordinate%5D%20%7Ba%7D%3B%0A%20%20%20%20%5Cnode%20%5Bint%5D%20(c)%20%5Bright%20of%3Da%5D%20%7B%24%5Cdownarrow%20M%24%7D%3B%0A%20%20%20%20%5Cnode%20%5Bcoordinate%5D%20(end)%20%5Bright%20of%3Dc%2C%20node%20distance%3D4.5cm%5D%7B%7D%3B%0A%20%20%20%20%5Cpath%5B-%3E%5D%20(b)%20edge%20node%20%7B%24x%5Bn%5D%24%7D%20(a)%3B%0A%20%20%20%20%5Cpath%5B-%3E%5D%20(a)%20edge%20node%20%7B%24x_%7B%5Comega_%7Bco%7D%7D%5Bn%5D%24%7D%20(c)%3B%0A%20%20%20%20%5Cdraw%5B-%3E%5D%20(c)%20edge%20node%20%7B%24x_d%5Bn%5D%3Dx%5BnM%5D%24%7D%20(end)%20%3B%0A%5Cend%7Btikzpicture%7D%0A%5Cend%7Bdocument%7D%0A" alt="\usetikzlibrary{arrows}
\begin{document}
\pagestyle{empty}
\tikzstyle{int}=[draw, fill=gray!8, minimum size=5em]
\tikzstyle{init} = [edge={to-,thin,black}]
\begin{tikzpicture}[node distance=5.5cm,auto,&gt;=latex']
    \node [int] (a) {$\begin{gathered}\text{L.P.F.}\\ Gain=1\\\omega_{co}=\pi/M\end{gathered}$};
    \node (b) [left of=a,node distance=4cm, coordinate] {a};
    \node [int] (c) [right of=a] {$\downarrow M$};
    \node [coordinate] (end) [right of=c, node distance=4.5cm]{};
    \path[-&gt;] (b) edge node {$x[n]$} (a);
    \path[-&gt;] (a) edge node {$x_{\omega_{co}}[n]$} (c);
    \draw[-&gt;] (c) edge node {$x_d[n]=x[nM]$} (end) ;
\end{tikzpicture}
\end{document}
" />

Now let's take an <em>e.g.</em>

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20%5Csum_%7Bn%3D-25%7D%20%5E%7B25%7D%20%5Cbig(%5Cbig2%5Cfrac%20%7Bsin(%5Cfrac%7B8n%7D%7B%5Cpi%7D)%7D%7Bn%7D%5Cbig)%5E%5Cbig2" alt="x[n] = \sum_{n=-25} ^{25} \big(\big2\frac {sin(\frac{8n}{\pi})}{n}\big)^\big2" />

That can be written as:

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20%5Cbig%5Bsinc(n%5Ccdot%20%5Cfrac%7B%5Cpi%7D%7B8%7D)%5Cbig%5D%5E%5Cbig2%20%5Ccdot%20%5Cbig%5B8%2F2%5Cpi%5Cbig%5D%5E%5Cbig2" alt="x[n] = \big[sinc(n\cdot \frac{\pi}{8})\big]^\big2 \cdot \big[8/2\pi\big]^\big2" />

<img src="https://i.upmath.me/svg/Where%20%5C%3B%20n%20%5Cin%20%5Cmathbb%7BZ%7D%5C%3B%7C%5C%3B%20n%5Cin%5B-25%2C25%5D" alt="Where \; n \in \mathbb{Z}\;|\; n\in[-25,25]" />

 Now we could run the simulation on MATLAB and Python and get:

[MATLAB]: remark it was developed using of the MATLAB Signal Processing Toolbox

![](MATLAB/Graphs/matlab_full.jpg)

[Python]: remark it was developed using numpy, matplotlib and scipy libraries

![](python/Graphs/python_full.png)

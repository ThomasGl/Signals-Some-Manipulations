# Signals-and-some-manipulations

**Let's Get Started**

## Start: 

Let's assume we are given a signal x(t), continuous and differentiable.

<em>exempli gratia</em> :

<img src="https://i.upmath.me/svg/x(t)%20%3D%20sin(t)" alt="x(t) = sin(t)" />

Now, regarding a practical analysis we can't generate a signal such that we get infinite precision. Thus, to address the signals in real life we can use sampling methods that shall render our signal in a very good approximation. Such a method will convert our signal from a continuous domain to a discrete one.

Also let us define a sampling interval T, and we will get a discrete signal x. Formulated as:

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20x(nT)" alt="x[n] = x(nT)" />

Sampling Example:

In signal processing some tools are introduced for various reasons and to assist in different scenarios. Some of which are: Upsampling, Downsampling, Interpolating and Decimating.

Their definitions are given as:

Upsampling: 

<img src="https://i.upmath.me/svg/x_i%5Bn%5D%20%3D%20x(nT%2FL)" alt="x_i[n] = x(nT/L)" />

Downsampling:

<img src="https://i.upmath.me/svg/x_d%5Bn%5D%20%3D%20x(nMT)" alt="x_d[n] = x(nMT)" />

Interpolating: 

We design a system using upsampling, such is given as:

Decimating:

We design a system using downsampling, given by:

Now let's take an <em>e.g.</em>

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20%5Csum_%7Bn%3D-25%7D%20%5E%7B25%7D%20%5Cbig(%5Cbig2%5Cfrac%20%7Bsin(%5Cfrac%7B8n%7D%7B%5Cpi%7D)%7D%7Bn%7D%5Cbig)%5E%5Cbig2" alt="x[n] = \sum_{n=-25} ^{25} \big(\big2\frac {sin(\frac{8n}{\pi})}{n}\big)^\big2" />

That can be written as:

<img src="https://i.upmath.me/svg/x%5Bn%5D%20%3D%20%5Cbig%5Bsinc(n%5Ccdot%20%5Cfrac%7B%5Cpi%7D%7B8%7D)%5Cbig%5D%5E%5Cbig2%20%5Ccdot%20%5Cbig%5B8%2F2%5Cpi%5Cbig%5D%5E%5Cbig2" alt="x[n] = \big[sinc(n\cdot \frac{\pi}{8})\big]^\big2 \cdot \big[8/2\pi\big]^\big2" />

<img src="https://i.upmath.me/svg/Where%20%5C%3B%20n%20%5Cin%20%5Cmathbb%7BZ%7D%5C%3B%7C%5C%3B%20n%5Cin%5B-25%2C25%5D" alt="Where \; n \in \mathbb{Z}\;|\; n\in[-25,25]" />

 Now we could run the simulation on MATLAB and Python and get:

[MATLAB]:


[Python]:

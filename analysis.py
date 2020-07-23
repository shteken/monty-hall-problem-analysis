import monty_hall_problem as mhp
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

def distribition_monty_hall(iters = 100, n = 1000):
    results = []
    for _ in range(iters):
        results.append(mhp.simulate_monty_hall(n))
    return results

def hist(results):
    hist = np.histogram(results)
    dist = stats.rv_histogram(hist)
    return dist

def plot_hist(results, ax=plt):
    ax.hist(results, label='Histogram')

def plot_cdf(dist, ax=plt):
    x = np.linspace(0, 1, 100)
    y_cdf = dist.cdf(x)  
    ax.plot(x, y_cdf, label='CDF')

def mean_std(results):
    mean = np.mean(results)
    std = np.std(results, ddof=1)
    return mean, std

def plot_npp(results, ax=plt): # Normal probability plot
    iter = len(results)
    normal_values = np.sort(np.random.normal(size=iter))
    x = np.linspace(-3, 3, iter+1)
    #print(x)
    mean, std = mean_std(results)
    y = std * x + mean # line from the distribution
    #print(y)
    ax.plot(normal_values, np.sort(results))
    ax.plot(x, y)

def estimates(dist):
    ci = round(dist.ppf(0.05),4), round(dist.ppf(0.95), 4) # confidence interval
    median = round(dist.ppf(0.5), 4)
    mean = round(dist.mean(), 4)
    std = round(dist.std(), 4)
    return mean, std, ci, median
    #print('Mean:', mean,'STD:', std, 'Confidence Interval:', ci, 'Median:', median)

def estimate_analytic(ns): #no iterations
    p = 1 /3
    dict_estimates = {}
    for n in ns:
        sigma = np.sqrt((p) * (1 - p) / n)
        dict_estimates[n] = (p, sigma)
        df = pd.DataFrame.from_dict(dict_estimates, orient='index', columns=['Mean', 'STD'])
        df = df.rename_axis(index='n')
    return df

def matrix_plot(ns, iters, func):
    len_ns = len(ns)
    len_iters = len(iters)
    fig, axs = plt.subplots(len_ns, len_iters)
    for n_id, n in enumerate(ns):
        for iter_id, iter in enumerate(iters):
            #print('n: ', n, 'iter: ', iter)
            if func == plot_npp or func == plot_hist:
                dist = distribition_monty_hall(iter, n)
            else:
                dist = hist(distribition_monty_hall(iter, n))
            func(dist, axs[n_id, iter_id])
            if iter_id == 0:
                axs[n_id, iter_id].set_ylabel(f'n = {n}')
            if n_id == 0:
                axs[n_id, iter_id].set_title(f'iter = {iter}')
    fig.tight_layout()
    plt.show()

def print_estimates(ns, iters):
    dict_estimates = {}
    for n in ns:
        dict_help = {}
        for iter in iters:
            dist = hist(distribition_monty_hall(iter, n))
            dict_help[iter] = estimates(dist)
        dict_estimates[n] = dict_help
    df = pd.DataFrame.from_dict(dict_estimates, orient='index')
    df = df.rename_axis(index='n', columns='iter')
    df.loc[0] = [('Mean', 'STD', 'Confidence Interval', 'Median') for iter in iters]
    df = df.sort_index()
    print(df)

ns = [10, 100, 1000]
iters = [10, 100, 1000]

matrix_plot(ns, iters, plot_hist)
matrix_plot(ns, iters, plot_cdf)
matrix_plot(ns, iters, plot_npp)

print('--- analytical solution per n ---')
print(estimate_analytic(ns))

print('--- estimated solution per n and iter ---')
print_estimates(ns, iters)

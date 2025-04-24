def create_page_rank_markov_chain(links, damping_factor=0.15):
    """По веб-графу со списком ребер links строит матрицу
    переходных вероятностей соответствующей марковской цепи.

        links --- список (list) пар вершин (tuple),
                может быть передан в виде numpy.array, shape=(|E|, 2);
        damping_factor --- вероятность перехода не по ссылке (float);

        Возвращает prob_matrix --- numpy.array, shape=(|V|, |V|).
    """
    links = np.array(links)
    N = links.max() + 1  # Число веб-страниц

    prob_matrix = np.full((N, N), damping_factor / N)

    for i in range(N):
        outgoing_links = links[links[:, 0] == i][:, 1]
        num_outgoing = len(outgoing_links)

        if num_outgoing > 0:
            prob_matrix[i, outgoing_links] += (1 - damping_factor) / num_outgoing

    prob_matrix = np.nan_to_num(prob_matrix, nan=damping_factor / N)

    return prob_matrix


def page_rank(
    links,
    start_distribution,
    damping_factor=0.15,
    tolerance=10 ** (-7),
    return_trace=False,
    max_iterations=10000,
):
    """Вычисляет веса PageRank для веб-графа со списком ребер links
    степенным методом, начиная с начального распределения start_distribution,
    доводя до сходимости с точностью tolerance.

        links --- список (list) пар вершин (tuple),
                может быть передан в виде numpy.array, shape=(|E|, 2);
        start_distribution --- вектор размерности |V| в формате numpy.array;
        damping_factor --- вероятность перехода не по ссылке (float);
        tolerance --- точность вычисления предельного распределения;
        return_trace --- если указана, то возвращает список распределений во
                            все моменты времени до сходимости

        Возвращает:
        1). если return_trace == False, то возвращает distribution ---
        приближение предельного распределения цепи,
        которое соответствует весам PageRank.
        Имеет тип numpy.array размерности |V|.
        2). если return_trace == True, то возвращает также trace ---
        список распределений во все моменты времени до сходимости.
        Имеет тип numpy.array размерности
        (количество итераций) на |V|.
    """

    prob_matrix = create_page_rank_markov_chain(links, damping_factor)
    distribution = np.array(start_distribution)  
    trace = []

    Pi_prev = distribution @ prob_matrix
    trace.append(Pi_prev)

    for iteration in range(max_iterations):  # Исправленный цикл
        distribution = Pi_prev @ prob_matrix
        trace.append(distribution)

        if np.linalg.norm(distribution - Pi_prev) < tolerance:
            break
        Pi_prev = distribution
    else:
        raise ValueError(f"Алгоритм PageRank не сошелся за {max_iterations} итераций.")

    if return_trace:
        return distribution.ravel(), np.array(trace)
    else:
        return distribution.ravel()
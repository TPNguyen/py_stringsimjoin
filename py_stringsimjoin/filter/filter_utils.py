from math import ceil
from math import floor
from math import sqrt
from sys import maxsize


def get_size_lower_bound(num_tokens, sim_measure_type, threshold):
    if sim_measure_type == 'COSINE':
        return int(ceil(round(threshold * threshold * num_tokens, 4)))
    elif sim_measure_type == 'DICE':
        return int(ceil(round((threshold / (2 - threshold)) * num_tokens, 4)))
    elif sim_measure_type == 'EDIT_DISTANCE':
        return num_tokens - threshold
    elif sim_measure_type == 'JACCARD':
        return int(ceil(round(threshold * num_tokens, 4)))
    elif sim_measure_type == 'OVERLAP':
        return threshold


def get_size_upper_bound(num_tokens, sim_measure_type, threshold):
    if sim_measure_type == 'COSINE':
        return int(floor(round(num_tokens / (threshold * threshold), 4)))
    elif sim_measure_type == 'DICE':
        return int(floor(round(
            ((2 - threshold) / threshold) * num_tokens, 4)))
    elif sim_measure_type == 'EDIT_DISTANCE':
        return num_tokens + threshold
    elif sim_measure_type == 'JACCARD':
        return int(floor(round(num_tokens / threshold, 4)))
    elif sim_measure_type == 'OVERLAP':
        return maxsize


def get_prefix_length(num_tokens, sim_measure_type, threshold, tokenizer):
    if num_tokens == 0:
        return 0

    if sim_measure_type == 'COSINE':
        return int(num_tokens -
                   ceil(threshold * threshold * num_tokens) + 1)
    elif sim_measure_type == 'DICE':
        return int(num_tokens -
                   ceil((threshold / (2 - threshold)) * num_tokens) + 1)
    elif sim_measure_type == 'EDIT_DISTANCE':
        return min(tokenizer.qval * threshold + 1, num_tokens)
    elif sim_measure_type == 'JACCARD':
        return int(num_tokens - ceil(threshold * num_tokens) + 1)
    elif sim_measure_type == 'OVERLAP':
        return max(num_tokens - threshold + 1, 0)


def get_overlap_threshold(l_num_tokens, r_num_tokens,
                          sim_measure_type, threshold, tokenizer):
    if sim_measure_type == 'COSINE':
        return ceil(round(threshold * sqrt(l_num_tokens * r_num_tokens), 4))
    elif sim_measure_type == 'DICE':
        return ceil(round((threshold / 2) * (l_num_tokens + r_num_tokens), 4))
    elif sim_measure_type == 'EDIT_DISTANCE':
        return max(l_num_tokens + tokenizer.qval - 1,
                   r_num_tokens + tokenizer.qval - 1) - tokenizer.qval + 1 - \
               tokenizer.qval * threshold
    elif sim_measure_type == 'JACCARD':
        return ceil(round((threshold / (1 + threshold)) * (l_num_tokens + r_num_tokens), 4))
    elif sim_measure_type == 'OVERLAP':
        return threshold

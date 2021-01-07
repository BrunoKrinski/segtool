import torch


def _take_channels(*xs, ignore_channels=None):
    if ignore_channels is None:
        return xs
    else:
        channels = [channel for channel in range(xs[0].shape[1]) if channel not in ignore_channels]
        xs = [torch.index_select(x, dim=1, index=torch.tensor(channels).to(x.device)) for x in xs]
        return xs


def _threshold(x, threshold=None):
    if threshold is not None:
        return (x > threshold).type(x.dtype)
    else:
        return x


def iou(pr, gt, eps=1e-7, threshold=None, ignore_channels=None, num_classes=None):
    """Calculate Intersection over Union between ground truth and prediction
    Args:
        pr (torch.Tensor): predicted tensor
        gt (torch.Tensor):  ground truth tensor
        eps (float): epsilon to avoid zero division
        threshold: threshold for outputs binarization
    Returns:
        float: IoU (Jaccard) score
    """

    pr = _threshold(pr, threshold=threshold)
    pr, gt = _take_channels(pr, gt, ignore_channels=ignore_channels)
    '''
    intersection = torch.sum(gt * pr)
    union = torch.sum(gt) + torch.sum(pr) - intersection + eps
    return (intersection + eps) / union
    '''
    if num_classes == None:
        ious = []
        for prs, gts in zip(pr, gt):
            for pr, gt in zip(prs, gts):
                intersection = torch.sum(gt * pr)
                union = torch.sum(gt) + torch.sum(pr) - intersection + eps
                iou_score = (intersection + eps) / union
                ious.append(iou_score)
        return sum(ious) / len(ious)
    else:
        ious = [0.0] * num_classes
        batch_size = len(pr)
        for prs, gts in zip(pr, gt):
            for i, pr, gt in zip(range(num_classes), prs, gts):
                intersection = torch.sum(gt * pr)
                union = torch.sum(gt) + torch.sum(pr) - intersection + eps
                iou_score = (intersection + eps) / union
                ious[i] += iou_score / batch_size
        return ious


jaccard = iou


def f_score(pr, gt, beta=1, eps=1e-7, threshold=None, ignore_channels=None, num_classes=None):
    """Calculate F-score between ground truth and prediction
    Args:
        pr (torch.Tensor): predicted tensor
        gt (torch.Tensor):  ground truth tensor
        beta (float): positive constant
        eps (float): epsilon to avoid zero division
        threshold: threshold for outputs binarization
    Returns:
        float: F score
    """

    pr = _threshold(pr, threshold=threshold)
    pr, gt = _take_channels(pr, gt, ignore_channels=ignore_channels)
    '''
    tp = torch.sum(gt * pr)
    fp = torch.sum(pr) - tp
    fn = torch.sum(gt) - tp

    score = ((1 + beta ** 2) * tp + eps) \
            / ((1 + beta ** 2) * tp + beta ** 2 * fn + fp + eps)

    return score'''
    if num_classes == None:
        scores = []
        for prs, gts in zip(pr, gt):
            for pr, gt in zip(prs, gts):
                tp = torch.sum(gt * pr)
                fp = torch.sum(pr) - tp
                fn = torch.sum(gt) - tp
                #score = ((1 + beta ** 2) * tp + eps) / ((1 + beta ** 2) * tp + beta ** 2 * fn + fp + eps)
                #precision = tp / (tp + fp + eps)
                #recall = tp / (tp + fn + eps) 
                score = tp / (tp + (fp + fn) / 2 + eps) 
                #score = 2 * (precision * recall) / (precision + recall + eps)
                scores.append(score)
        return sum(scores) / len(scores)
    else:
        scores = [0.0] * num_classes
        batch_size = len(pr)
        for prs, gts in zip(pr, gt):
            #print('--------------------')
            for i, pr, gt in zip(range(num_classes), prs, gts):
                tp = torch.sum(gt * pr)
                #print('tp:' + str(tp))
                fp = torch.sum(pr) - tp
                #print('fp:' + str(fp))
                fn = torch.sum(gt) - tp
                #print('fn:' + str(fn))
                #score = ((1 + beta ** 2) * tp + eps) / ((1 + beta ** 2) * tp + beta ** 2 * fn + fp + eps)
                #precision = tp / (tp + fp + eps)
                #recall = tp / (tp + fn + eps) 
                score = tp / (tp + (fp + fn) / 2 + eps)
                #score = 2 * (precision * recall) / (precision + recall + eps) 
                #print((1 + beta ** 2) * tp + eps)
                #print((1 + beta ** 2) * tp + beta ** 2 * fn + fp + eps)
                #print('score:' + str(score))
                scores[i] += score / batch_size
            #print('--------------------')
        return scores


def accuracy(pr, gt, threshold=0.5, ignore_channels=None):
    """Calculate accuracy score between ground truth and prediction
    Args:
        pr (torch.Tensor): predicted tensor
        gt (torch.Tensor):  ground truth tensor
        eps (float): epsilon to avoid zero division
        threshold: threshold for outputs binarization
    Returns:
        float: precision score
    """
    pr = _threshold(pr, threshold=threshold)
    pr, gt = _take_channels(pr, gt, ignore_channels=ignore_channels)

    tp = torch.sum(gt == pr, dtype=pr.dtype)
    score = tp / gt.view(-1).shape[0]
    return score


def precision(pr, gt, eps=1e-7, threshold=None, ignore_channels=None):
    """Calculate precision score between ground truth and prediction
    Args:
        pr (torch.Tensor): predicted tensor
        gt (torch.Tensor):  ground truth tensor
        eps (float): epsilon to avoid zero division
        threshold: threshold for outputs binarization
    Returns:
        float: precision score
    """

    pr = _threshold(pr, threshold=threshold)
    pr, gt = _take_channels(pr, gt, ignore_channels=ignore_channels)

    tp = torch.sum(gt * pr)
    fp = torch.sum(pr) - tp

    score = (tp + eps) / (tp + fp + eps)

    return score


def recall(pr, gt, eps=1e-7, threshold=None, ignore_channels=None):
    """Calculate Recall between ground truth and prediction
    Args:
        pr (torch.Tensor): A list of predicted elements
        gt (torch.Tensor):  A list of elements that are to be predicted
        eps (float): epsilon to avoid zero division
        threshold: threshold for outputs binarization
    Returns:
        float: recall score
    """

    pr = _threshold(pr, threshold=threshold)
    pr, gt = _take_channels(pr, gt, ignore_channels=ignore_channels)

    tp = torch.sum(gt * pr)
    fn = torch.sum(gt) - tp

    score = (tp + eps) / (tp + fn + eps)

    return score

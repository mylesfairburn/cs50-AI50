import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    linkedPages = corpus[page]

    if not linkedPages:
        return {pageName: 1 / len(corpus) for pageName in corpus}
    
    pagesProb = dict()
    for pageName in corpus:
        prob = (1 - damping_factor) / len(corpus)
        if pageName in linkedPages:
            prob += damping_factor / len(linkedPages)

        pagesProb.update({pageName: prob})

    totalProb = 0
    for item in pagesProb.values():
        totalProb += item

    if abs(totalProb - 1) < 0.0001:  # Check probability adds to one
        return pagesProb
    else:
        raise Exception("Linked pages probabilities did not add to 1.")


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    currentPage = random.choice(list(corpus))
    pageRanks = dict()
    for i in range(n):
        resultingProbs = transition_model(corpus, currentPage, damping_factor)
        if not currentPage in pageRanks:
            pageRanks.update({currentPage: 1})
        else:
            pageRanks[currentPage] += 1

        randProb = random.random()
        totalSeenProb = 0
        for page, probability in resultingProbs.items():
            totalSeenProb += probability
            if randProb < totalSeenProb:
                currentPage = page
                break

    for page, rank in pageRanks.items():
        pageRanks[page] = rank / n

    pageRankSum = 0
    for probability in pageRanks.values():
        pageRankSum += probability

    if abs(pageRankSum - 1) < 0.0001:
        return pageRanks
    else:
        raise Exception("Page rank probabilities did not add to 1.")


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    numPages = len(corpus)
    pageRanks = {page: 1 / numPages for page in corpus}

    converged = False
    while not converged:
        converged = True
        newRanks = dict()

        for page in corpus:
            total = 0
            for candidate, links in corpus.items():
                if not links:
                    total += pageRanks[candidate] / numPages
                elif page in links:
                    total += pageRanks[candidate] / len(links)

            newRanks[page] = (1 - damping_factor) / numPages + damping_factor * total

        for page in corpus:
            if abs(newRanks[page] - pageRanks[page]) > 0.001:
                converged = False

        pageRanks = newRanks

    pageRankSum = 0
    for probability in pageRanks.values():
        pageRankSum += probability

    if abs(pageRankSum - 1) < 0.0001:  # Check probability adds to one
        return pageRanks
    else:
        raise Exception("Page rank probabilities did not add to 1.")


if __name__ == "__main__":
    main()

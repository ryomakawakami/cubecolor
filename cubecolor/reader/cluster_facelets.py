from scipy.cluster.vq import kmeans, vq

def clusterFacelets(facelets):
    try:
        codebook, _ = kmeans([facelet[2] for facelet in facelets], 3)
        cluster_indices, _ = vq([facelet[2] for facelet in facelets], codebook)

        clusters = [[], [], []]
        for i, facelet in enumerate(facelets):
            clusters[cluster_indices[i]].append(facelet)

        return clusters
    except:
        return None
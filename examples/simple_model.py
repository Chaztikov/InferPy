import tensorflow as tf
from tensorflow_probability import edward2 as ed
import inferpy as inf



@inf.probmodel
def simple():
    theta = inf.Normal(0, 1, name="theta")
    with inf.datamodel():
        x = inf.Normal(theta, 2, name="x")


@inf.probmodel
def q_model():
    qtheta_loc = inf.Parameter(1., name="qtheta_loc")
    qtheta_scale = tf.math.softplus(inf.Parameter(1., name="qtheta_scale"))

    qtheta = inf.Normal(qtheta_loc, qtheta_scale, name="theta")



## example of use ###
# generate training data
N = 1000
sess = tf.Session()
x_train = sess.run(ed.Normal(5., 2.).distribution.sample(N))



##

m = simple()
#
VI = inf.inference.VI(q_model(), epochs=1000)
m.fit({"x": x_train}, VI)


####
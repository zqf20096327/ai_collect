Unlearning via Bad-Teacher Distillation and Temperature Analysis

This repository investigates machine unlearning using a bad teacher–student distillation framework, with a particular focus on:

Influence of temperature (τ) in the bad-teacher KD loss

Unlearning effectiveness across different τ values

Model compression by distilling a large teacher into a smaller student

Practical unlearning pipelines implemented in shell scripts (.sh)

Experiment logs stored for reproducibility

We mainly evaluate ResNet-18 as the student model on CIFAR-10

Project Motivation

Machine unlearning aims to remove the influence of a subset of data (“forget set”) from a trained model.
We explore a Bad Teacher Distillation strategy:

A good teacher provides general knowledge for retention.

A bad teacher intentionally misguides the model for the forget set.

The temperature τ controls the softness of teacher logits.

We hypothesized that adjusting τ would affect:

Forget acc

Retain accuracy

MIA protection

Logit entropy alignment

However, our experiments show no clear monotonic tendency with respect to τ when using ResNet-18, indicating that τ alone does not sufficiently control the forgetting strength for this architecture.

Unlearning via Bad-Teacher Distillation and Unified Compression–Unlearning

This repository investigates machine unlearning and model compression using a unified teacher–student distillation framework.
Our experiments focus on:

Influence of temperature (τ) in bad-teacher distillation

Unified stage compression + unlearning

Trade-offs between forget accuracy and test accuracy

Practical training scripts (.sh) and experiment logs

We mainly evaluate ResNet-18 student models on CIFAR-10.

🔍 Project Motivation

Traditional unlearning and model compression are often treated as two separate tasks:

First: train a large model

Then: unlearn

Finally: compress

However, doing them independently introduces redundant computation and can even reintroduce forgotten information during compression.

To address this, we propose a unified stage:

Compress + Unlearn simultaneously by distilling a student directly from both good and bad teachers.

This avoids retraining steps and allows us to analyze how compression interacts with forget-set unlearning.

 Key Contributions
 1. Temperature (τ) Analysis in Bad-Teacher KD

We tested various τ values to understand how the softening of logits affects unlearning performance.
Surprisingly, no strong monotonic tendency was observed when using ResNet-18, implying τ alone is not a dominant factor.

 2. Unified Stage: Compression + Unlearning

Instead of applying unlearning and compression separately, we combine them into a single distillation stage:

Good teacher → transfers general knowledge

Bad teacher → removes information related to forget set

Student model → learns a compressed representation while unlearning simultaneously

This greatly simplifies the pipeline and reduces computation.

3. Trade-off Between Forget Accuracy and Test Accuracy

When unlearning and compressing simultaneously:

Lower forget accuracy = better unlearning

Higher test accuracy = better generalization

These two metrics naturally conflict during unified distillation.

Our experiments show:

There exists a clear trade-off between forget accuracy and test accuracy.

This is expected because stronger forgetting often forces the student away from generalizable representations.

 4. Why Test Accuracy Matters More Than Retain Accuracy

In standard unlearning research, retain accuracy is an important indicator of how much useful knowledge remains.
However, when performing compression:

The student model already has reduced capacity


Test accuracy is the ultimate metric for compressed model usability

Because the final student is intended to be deployed, test accuracy becomes more crucial than retain accuracy.

Thus, in our unified compression–unlearning framework:

Test accuracy is prioritized over retain accuracy.

This aligns with realistic goals in model deployment, where performance on unseen data is more critical.


nohup python -m unlearn_kd.scripts.unlearn_kd \
  --good_teacher resnet50 \
  --student resnet18 \
  --good_ckpt $CKPT_DIR/teachers/ckpt_r50.pt \
  --T 1.0 --alpha_retain 0.8 --alpha_unlearn 1.0 \
  --ce_scale_unlearn 0.0 \
  --student_pretrained True \
  --student_ckpt $CKPT_DIR/students/ckpt_r18_r50_kd.pt \
  --save $CKPT_DIR/unlearn_kd/ckpt_r18_r50_ukd.pt \
  --device 3 \
  > $LOG_DIR/ukd_r18_from_r50.log 2>&1 &







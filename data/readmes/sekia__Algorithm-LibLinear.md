=head1 NAME

Algorithm::LibLinear - A Perl binding for LIBLINEAR, a library for classification, regression, and outlier detection using linear Support Vector Machines (SVM) and logistic regression

=head1 SYNOPSIS

  use Algorithm::LibLinear;

  # Instantiate a learner for L2-regularized L2-loss support vector classification (SVC).
  my $learner = Algorithm::LibLinear->new(
    cost => 1,
    epsilon => 0.01,
    solver => 'L2R_L2LOSS_SVC',
    weights => [
      +{ label => 1, weight => 1, },
      +{ label => -1, weight => 1, },
    ],
  );

  # Load a training dataset from the DATA filehandle.
  my $data_set = Algorithm::LibLinear::DataSet->load(fh => \*DATA);

  # Automatically find optimal parameters.
  $learner->find_parameters(data_set => $data_set, num_folds => 5, update => 1);

  # Perform cross-validation to evaluate performance.
  my $accuracy = $learner->cross_validation(data_set => $data_set, num_folds => 5);

  # Train the model on the dataset.
  my $classifier = $learner->train(data_set => $data_set);

  # Predict the class label (+1 or -1) for a given feature vector.
  my $class_label = $classifier->predict(feature => +{ 1 => 0.38, 2 => -0.5, ... });
  
  __DATA__
  +1 1:0.708333 2:1 3:1 4:-0.320755 5:-0.105023 6:-1 7:1 8:-0.419847 9:-1 10:-0.225806 12:1 13:-1 
  -1 1:0.583333 2:-1 3:0.333333 4:-0.603774 5:1 6:-1 7:1 8:0.358779 9:-1 10:-0.483871 12:-1 13:1 
  +1 1:0.166667 2:1 3:-0.333333 4:-0.433962 5:-0.383562 6:-1 7:-1 8:0.0687023 9:-1 10:-0.903226 11:-1 12:-1 13:1 
  -1 1:0.458333 2:1 3:1 4:-0.358491 5:-0.374429 6:-1 7:-1 8:-0.480916 9:1 10:-0.935484 12:-0.333333 13:1 
  -1 1:0.875 2:-1 3:-0.333333 4:-0.509434 5:-0.347032 6:-1 7:1 8:-0.236641 9:1 10:-0.935484 11:-1 12:-0.333333 13:-1 
  ...

=head1 DESCRIPTION

C<Algorithm::LibLinear> is an XS binding for LIBLINEAR, a fast C/C++ library for linear classification, regression, and outlier detection.

This version is compatible with LIBLINEAR 2.48, released on January 5, 2025.

=head1 METHODS

=head2 new([bias => -1.0] [, cost => 1] [, epsilon => undef] [, loss_sensitivity => 0.1] [, nu => 0.5] [, regularize_bias => 1] [, recalculate_weights => 0] [, solver => 'L2R_L2LOSS_SVC_DUAL'] [, weights => []])

Constructor. Accepts the following optional named parameters, also accessible via getter methods of the same name.

=over 4

=item bias

The bias term added to feature vectors (corresponding to the C<-B> option of the LIBLINEAR C<train> command). This term is active only when its value is positive.

=item cost

The penalty parameter C (corresponding to the C<-c> option).

=item epsilon

The tolerance of the termination criterion (corresponding to the C<-e> option). The default depends on the chosen C<solver>.

=item loss_sensitivity

The epsilon parameter (p) in the loss function of Support Vector Regression (SVR), corresponding to the C<-p> option.

=item nu

The nu parameter for one-class SVM (corresponding to the C<-n> option).

=item regularize_bias

A boolean indicating whether to include the bias term in regularization (corresponding to the negation of the C<-R> option). Defaults to true.

=item recalculate_weights

A boolean indicating whether to recalculate class weights dynamically. This option is valid only for the dual solvers of L2-regularized L1- or L2-loss Support Vector Classifiers (C<L2R_L1LOSS_SVC_DUAL> and C<L2R_L2LOSS_SVC_DUAL>).

=item solver

The solver type to use (corresponding to the C<-s> option).

Supported solvers for classification:

=over 4

=item * 'L2R_LR' - L2-regularized logistic regression

=item * 'L2R_L2LOSS_SVC_DUAL' - L2-regularized L2-loss SVC (dual)

=item * 'L2R_L2LOSS_SVC' - L2-regularized L2-loss SVC (primal)

=item * 'L2R_L1LOSS_SVC_DUAL' - L2-regularized L1-loss SVC (dual)

=item * 'MCSVM_CS' - Crammer and Singer multi-class SVM

=item * 'L1R_L2LOSS_SVC' - L1-regularized L2-loss SVC

=item * 'L1R_LR' - L1-regularized logistic regression (primal)

=item * 'L2R_LR_DUAL' - L2-regularized logistic regression (dual)

=back

Supported solvers for regression:

=over 4

=item * 'L2R_L2LOSS_SVR' - L2-regularized L2-loss SVR (primal)

=item * 'L2R_L2LOSS_SVR_DUAL' - L2-regularized L2-loss SVR (dual)

=item * 'L2R_L1LOSS_SVR_DUAL' - L2-regularized L1-loss SVR (dual)

=back

Supported solvers for outlier detection:

=over 4

=item * 'ONECLASS_SVM' - One-class SVM

=back

=item weights

An array reference used to adjust the penalty cost for specific classes (corresponding to the C<-wi> option).

For example:

  my $learner = Algorithm::LibLinear->new(
    weights => [
      +{ label => 1, weight => 0.5 },
      +{ label => 2, weight => 1.0 },
      +{ label => 3, weight => 0.5 },
    ],
  );

This configuration doubles the penalty weight for class 2, making samples belonging to class 2 have twice the influence on training compared to those in classes 1 or 3.

This option is particularly useful for addressing class imbalance in the training dataset.

=back

=head2 cross_validation(data_set => $data_set, num_folds => $num_folds)

Evaluates training performance using N-fold cross-validation.
The dataset is partitioned into N equal-sized folds. For each fold, the model is trained on the remaining N-1 folds and evaluated on the held-out fold.

Returns the average classification accuracy for classification solvers, or the mean squared error (MSE) for regression solvers.

=head2 find_cost_parameter(data_set => $data_set, num_folds => $num_folds [, initial => -1.0] [, update => 0])

B<Deprecated.> Use C<find_parameters> instead.

A convenience wrapper around C<find_parameters> that tunes only the C<cost> parameter. Note that if C<update> is enabled, the C<loss_sensitivity> parameter may also be updated in the process.

=head2 find_parameters(data_set => $data_set, num_folds => $num_folds [, initial_cost => -1.0] [, initial_loss_sensitivity => -1.0] [, update => 0])

Finds the optimal hyperparameters using N-fold cross-validation. If C<initial_cost> or C<initial_loss_sensitivity> is negative, its optimal value is automatically determined.

This method is supported only by the C<'L2R_LR'>, C<'L2R_L2LOSS_SVC'>, and C<'L2R_L2LOSS_SVR'> solvers. It throws an exception if called when using any other solver.

If the C<update> parameter is true, the learner instance is updated in-place with the discovered parameters. This is disabled by default.

Returns an array reference containing three elements: the optimal C<cost>, the optimal C<loss_sensitivity> (which is C<undef> unless the solver is C<'L2R_L2LOSS_SVR'>), and the evaluation metric (average accuracy or MSE) achieved with these parameters.

=head2 train(data_set => $data_set)

Trains a model on the provided dataset and returns an L<Algorithm::LibLinear::Model> instance.
The C<data_set> argument must be an L<Algorithm::LibLinear::DataSet> instance.

=head1 AUTHOR

Koichi SATO E<lt>sekia@cpan.orgE<gt>

=head1 SEE ALSO

L<Algorithm::LibLinear::DataSet>

L<Algorithm::LibLinear::FeatureScaling>

L<Algorithm::LibLinear::Model>

L<LIBLINEAR Homepage|http://www.csie.ntu.edu.tw/~cjlin/liblinear/>

L<Algorithm::SVM> - A Perl binding to LIBSVM.

=head1 LICENSE

=head2 Algorithm::LibLinear

Copyright (c) 2013-2025 Koichi SATO. All rights reserved.

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ``AS IS'', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

=head2 LIBLINEAR

Copyright (c) 2007-2025 The LIBLINEAR Project.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither name of copyright holders nor the names of its contributors
may be used to endorse or promote products derived from this software
without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


=cut


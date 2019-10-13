import { Button, SpacedGroup } from '@dabapps/roe';
import React, { PureComponent } from 'react';
import { connect } from 'react-redux';

import { increment } from '^/actions';
import { StoreState } from '^/store/types';

interface StateProps {
  count: number;
}

interface DispatchProps {
  onClick: typeof increment;
}

type Props = StateProps & DispatchProps;

export class Counter extends PureComponent<Props> {
  public render() {
    return (
      <SpacedGroup block className="margin-vertical-base">
        <span>{this.props.count}</span>
        <Button className="primary hollow" onClick={this.props.onClick}>
          Increment
        </Button>
      </SpacedGroup>
    );
  }
}

export const mapStateToProps = ({ count }: StoreState) => ({
  count,
});

export default connect(
  mapStateToProps,
  { onClick: increment }
)(Counter);

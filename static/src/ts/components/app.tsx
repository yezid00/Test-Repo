import {
  AppRoot,
  Button,
  Container,
  Nav,
  NavBar,
  NavItem,
  SideBar,
} from '@dabapps/roe';
import React, { PureComponent } from 'react';
import { connect } from 'react-redux';

import { closeSideBar, openSideBar } from '^/actions/side-bar';
import Counter from '^/components/counter';
import { StoreState } from '^/store/types';

export type StateProps = Pick<StoreState, 'sideBarOpen'>;

export interface DispatchProps {
  onClickCloseSideBar: typeof closeSideBar;
  onClickOpenSideBar: typeof openSideBar;
}

export type Props = StateProps & DispatchProps;

export class App extends PureComponent<Props> {
  public render() {
    const { sideBarOpen } = this.props;

    return (
      <AppRoot>
        <NavBar>
          <Container>
            <strong>My name is Yezid</strong>
          </Container>
        </NavBar>
        <SideBar
          position="left"
          open={sideBarOpen}
          onClickOutside={this.props.onClickCloseSideBar}
        >
          <Nav>
            <NavItem active>
              <a>Home</a>
            </NavItem>
            <NavItem>
              <a>Go to a place</a>
            </NavItem>
            <NavItem>
              <a>Go to another place</a>
            </NavItem>
          </Nav>
        </SideBar>
        <Container>
          <h1>Hello, DabApps!</h1>
          <p>This is a project written in TypeScript!【ツ】</p>
          <Button
            className="primary hollow"
            onClick={this.props.onClickOpenSideBar}
          >
            Open SideBar
          </Button>
          <Counter />
        </Container>
      </AppRoot>
    );
  }
}

export const mapStateToProps = ({ sideBarOpen }: StoreState): StateProps => {
  return {
    sideBarOpen,
  };
};

export default connect(
  mapStateToProps,
  { onClickOpenSideBar: openSideBar, onClickCloseSideBar: closeSideBar }
)(App);
